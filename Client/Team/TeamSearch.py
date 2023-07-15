from Utils.Reader import BSMessageReader
from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
from Utils.Helpers import Helpers

class TeamSearch(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        #14199!!!#
        self.read_Vint()
    def process(self):
        for room in Helpers.rooms:
            if len(room['plrs']) <= 2:
                new_player = {'id': self.player.low_id, 'isOwner': 0, 'state': 2}
                room['plrs'].append(new_player)
                self.player.room_id = int(room['roomID'])
                DataBase.replaceValue(self, 'roomID', self.player.room_id)
                TeamMessage(self.client, self.player).send()
                break