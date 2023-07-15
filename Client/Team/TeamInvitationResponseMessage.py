from Utils.Reader import BSMessageReader
from Server.Team.TeamMessage import TeamMessage
from Utils.Helpers import Helpers
from database.DataBase import DataBase

class TeamInvitationResponseMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.Response = self.read_Vint();
        self.ID2 = self.read_int()#LOW_ID
        self.ID = self.read_int()#LOW_ID
    def process(self):
        if self.Response == 1:
            new_player = {'id': self.player.low_id, 'isOwner': 0, 'state': 2}
            for plr in Helpers.rooms[self.ID-1]['invites']:
                if plr['id'] == self.player.low_id:
                        plr['state'] = 1
            Helpers.rooms[self.ID-1]['plrs'].append(new_player)
            self.player.room_id = self.ID
            DataBase.replaceValue(self, 'roomID', self.player.room_id)
            TeamMessage(self.client, self.player).send()
        if self.Response == 2:
            for room in Helpers.rooms:
                if room['roomID'] == self.ID:
                    for invite in room['invites']:
                        if invite['id'] == self.ID:
                            invite['state'] = 2