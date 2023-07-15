from Utils.Writer import Writer
from Utils.BitStream import BitStream
from Server.Battle.BattleEnd2 import BattleEnd2
from Logic.Battle.GameObjectManager import GameObjectManager
class VisionUpdate(Writer):

	def __init__(self, client, player, my_battle):
		super().__init__(client)
		self.id = 24109
		self.player = player
		self.my_battle = my_battle


	def encode(self):
	
		self.writeVint(self.my_battle["battleTick"])
		self.writeVint(self.player.dudu)
		self.writeVint(0) # Commands Count
		self.writeVint(0) # spectators
		self.writeBoolean(False) # Live Boolean
		abc = -1
		if int(self.my_battle["battleTick"]) > 2525:
			abc = 2
			
		stream = BitStream()
		stream.writePositiveInt(1000000, 21)
		stream.writePositiveInt(0, 1)
		stream.writeInt(abc, 4) # понос
		if abc == 2:
			BattleEnd2(self.client, self.player, self.my_battle).send()
		GameObjectManager.encode(stream,self.my_battle,self)
		stream.writePositiveInt(0, 8)
		self.writeBytes(stream.getBuff())