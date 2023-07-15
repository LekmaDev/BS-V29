from Utils.Reader import BSMessageReader
from Server.Team.TeamMessage import TeamMessage
from Utils.Helpers import Helpers
from Server.Team.TeamInvitationMessage import TeamInvitationMessage

class TeamInviteMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.read_Vint()#highID
        self.ID = self.read_Vint()#lowID
    def process(self):
        for room in Helpers.rooms:
            if room['roomID'] == self.player.room_id:
                new_player = {'id': self.ID,'state': 0,'slot': 1}
                room['invites'].append(new_player)
                TeamMessage(self.client, self.player)