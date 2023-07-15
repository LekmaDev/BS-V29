from Utils.Reader import BSMessageReader
from Server.Team.TeamStream import TeamStream
from Utils.Helpers import Helpers
class TeamPremadeChatMessage(BSMessageReader):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.client = client
		self.player = player
        
	def decode(self):
		self.pin = self.read_Vint()
		self.Type = self.read_Vint()
	def process(self):
		self.player.ctick += 1
		for room in Helpers.rooms:
			if room['roomID'] == self.player.room_id:
				Helpers.rooms[self.player.room_id-1]['Tick'] += 1
				new_msg = {'id': self.player.low_id, 'Type': self.Type, 'pin': self.pin}
				room['Premade'].append(new_msg)
				TeamStream(self.client, self.player).send()
				break
        