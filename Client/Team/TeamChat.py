from Utils.Reader import BSMessageReader
from Server.Team.TeamStream2 import TeamStream2
from database.DataBase import DataBase
from Utils.Helpers import Helpers
import json
class TeamChat(BSMessageReader):
	#14369
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
		
	def decode(self):
		self.message = self.read_string()
		 
	def process(self):
		TeamStream2(self.client, self.player,self.player.low_id,self.player.name,self.message).send()
		for player in Helpers.rooms[self.player.room_id-1]['plrs']:
			Helpers.rooms[self.player.room_id-1]['Tick'] += 1
			TeamStream2(self.client, self.player,self.player.low_id,self.player.name,self.message).sendWithLowID(player['id'])
			break