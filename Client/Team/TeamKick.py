from Utils.Reader import BSMessageReader
from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
from Utils.Helpers import Helpers
from Server.Team.TeamLeaveOkMessage import TeamLeaveOkMessage
class TeamKick(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.read_Vint()#highID
        self.ID = self.read_Vint()#lowID
    def process(self):
        for player in Helpers.rooms[self.player.room_id-1]['plrs']:
            if player['id'] == self.ID:
                Helpers.rooms[self.player.room_id-1]['plrs'].remove(player)
                DataBase.replaceOtherValue(self, self.ID, "roomID", 0)
                TeamLeaveOkMessage(self.client, self.player).sendWithLowID(self.ID)
        if self.player.room_id > 0:
        	TeamMessage(self.client, self.player).send()