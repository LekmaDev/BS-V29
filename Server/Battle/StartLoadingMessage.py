from Utils.Writer import Writer
from database.DataBase import DataBase

class StartLoadingMessage(Writer):

	def __init__(self, client, player, my_battle):
		super().__init__(client)
		self.id = 20559
		self.player = player
		self.my_battle = my_battle
		
	def encode(self):
		self.writeInt(6) #6
		self.writeInt(0)
		self.writeInt(0)
		
		self.writeInt(6) #players count
		for i in range(3):
			self.writeInt(0) #High ID
			self.writeInt(self.my_battle["players"][0]["plrID"]) #Low ID
			self.writeVint(i)
			self.writeVint(0)
			self.writeVint(0)
			
			self.writeInt(0) #unk
			self.players = DataBase.loadbyID(self,self.my_battle["players"][0]["plrID"])
			self.writeScId(16, self.my_battle["players"][0]["BID"])
			self.writeScId(29, self.my_battle["players"][0]["SID"])
			self.writeByte(0)
			self.writeString(f"{self.players[2]}")
			self.writeVint(100)
			self.writeVint(28000000 + self.players[9])
			self.writeVint(43000000 + self.players[10])
		for i in range(3):
			self.writeInt(0) #High ID
			self.writeInt(self.my_battle["players"][1]["plrID"]) #Low ID
			self.writeVint(3+i)
			self.writeVint(1)
			self.writeVint(0)
			
			self.writeInt(0) #unk
			self.players2 = DataBase.loadbyID(self,self.my_battle["players"][1]["plrID"])
			self.writeScId(16, self.my_battle["players"][1]["BID"])
			self.writeScId(29, self.my_battle["players"][1]["SID"])
			self.writeByte(0)
			self.writeString(f"{self.players2[2]}")
			self.writeVint(100)
			self.writeVint(28000000 + self.players2[9])
			self.writeVint(43000000 + self.players2[10])
		#PLAYERS SLOT END#
		
		self.writeInt(0) #count...
		
		self.writeInt(0) #Count
		
		self.writeInt(0) # Unknown
		
		self.writeVint(0)#
		self.writeVint(1) #DrawMap
		self.writeVint(1)
		
		self.writeBoolean(True) #2, 39 - Spectating
		self.writeVint(0) # is Spectating
		self.writeVint(0)
		
		self.writeScId(15, 1) # map
		#Bountu - 1,219,218,82,54,4
		#Gem grab - 7,12
		self.writeBoolean(False)