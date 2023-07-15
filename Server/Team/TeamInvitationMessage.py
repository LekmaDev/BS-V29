from Utils.Writer import Writer
from database.DataBase import DataBase
import json
class TeamInvitationMessage(Writer):
	def __init__(self, client, player, ID=1, Inviter=3):
		super().__init__(client)
		self.id = 24589
		self.player = player
		self.ID = ID
		self.Inviter = Inviter
	def encode(self):
		self.writeVint(1) # Count
		self.writeInt(0)
		self.writeInt(self.ID)
		self.writeInt(0)
		self.writeInt(self.Inviter+3)
		self.players = DataBase.loadbyID(self,self.Inviter)
		for x in range(6):
			self.writeString()
		player = self.players
		brawlerData = json.loads(player[13])
		self.writeInt(brawlerData['highest_trophies']) # Trophies
		for x in range(4):
			self.writeInt(0)

		bool1 = True
		self.writeBoolean(True)
		self.writeInt(0)
		self.writeInt(3)
		self.writeInt(0)
		self.writeString()
		self.writeInt(0)
		self.writeInt(0)

		self.writeString()
		self.writeInt(0)
		self.writeBoolean(True)
		self.writeString(f"{self.players[2]}")
		self.writeVint(100)
		self.writeVint(28000000 + self.players[9])
		self.writeVint(43000000 + self.players[10])
		if self.players[20] == 1:
			self.writeVint(43000000 + self.players[10])
		else:
			self.writeVint(0)