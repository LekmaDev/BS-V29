import socket
import time
import os
from threading import *
import sqlite3
from database.DataBase import DataBase
from Logic.Device import Device
from Logic.Player import Players
from Logic.LogicMessageFactory import packets
from Logic.LobbyInfoMessage import LobbyInfoMessage
import json
def _(*args):
	print('[INFO]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()
addr = {}
block = []
class Server:
	Clients = {"ClientCounts": 0, "Clients": {}}
	ThreadCount = 0
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip
	def start(self):
		self.server.bind((self.ip, self.port))
		print(f'Server | Lobby started! {self.ip}:{self.port}')
		plrsinfo = "database/Player/plr.db"
		if os.path.exists(plrsinfo):
			conn = sqlite3.connect("database/Player/plr.db")
			c = conn.cursor()
			c.execute("UPDATE plrs SET roomID=0")
			c.execute("UPDATE plrs SET online=0")
			c.execute("SELECT * FROM plrs")
			conn.commit()
			conn.close()
		while True:
			self.server.listen()
			client, address = self.server.accept()
			if address[0] in addr:
				addr[address[0]] += 1
			else:
				addr[address[0]] = 0
			if address[0] in block:
				os.system(f"iptables -A INPUT -s {address[0]} -j DROP")
				client.close()
			elif addr[address[0]] >= 4:
				os.system(f"iptables -A INPUT -s {address[0]} -j DROP")
				block.append(address[0])
				config = open('config.json', 'r')
				content = config.read()
				settings = json.loads(content)
				settings['block'].append(address[0])
				print(f"{settings['block']}")
				client.close()
			else:
				ClientThread(client, address).start()
				Server.ThreadCount += 1
class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.device = Device(self.client)
		self.player = Players(self.device)

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				block.append(self.address[0])
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					LobbyInfoMessage(self.client, self.player, Server.ThreadCount).send()
					if packet_id in packets:
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()
						if packet_id == 10101:
							Server.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
							Server.Clients["ClientCounts"] = Server.ThreadCount
							self.player.ClientDict = Server.Clients
				if time.time() - last_packet > 6:
					addr[self.address[0]] = 0
					del addr[self.address[0]]
					DataBase.replaceValue(self, 'online', 0)
					Server.ThreadCount -= 1
					print(f"Player Online {Server.ThreadCount}")
					self.client.close()
					break
		except ConnectionAbortedError:
			addr[self.address[0]] = 0
			del addr[self.address[0]]
			DataBase.replaceValue(self, 'online', 0)
			Server.ThreadCount -= 1
			print(f"Player Online {Server.ThreadCount}")
			self.client.close()
		except ConnectionResetError:
			addr[self.address[0]] = 0
			del addr[self.address[0]]
			DataBase.replaceValue(self, 'online', 0)
			Server.ThreadCount -= 1
			print(f"Player Online {Server.ThreadCount}")
			self.client.close()
		except TimeoutError:
			addr[self.address[0]] = 0
			del addr[self.address[0]]
			DataBase.replaceValue(self, 'online', 0)
			Server.ThreadCount -= 1
			print(f"Player Online {Server.ThreadCount}")
			self.client.close()

if __name__ == '__main__':
	server = Server('0.0.0.0', 9339)
	server.start()