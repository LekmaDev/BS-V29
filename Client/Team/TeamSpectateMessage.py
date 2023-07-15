from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
from Server.Login.LoginFailedMessage import LoginFailedMessage
from Utils.Reader import BSMessageReader
import traceback
from Utils.Helpers import Helpers
import json
class TeamSpectateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client 
    def decode(self):
    	#14358!!#
        self.roomHigh = self.read_Vint()
        self.room_id = self.read_Vint()
        self.roomType = self.read_Vint()
    def process(self):
        for room in Helpers.rooms:
            if room['roomID'] == self.room_id:
                new_player = {'id': self.player.low_id, 'isOwner': 0, 'state': 2}
                room['plrs'].append(new_player)
                self.player.room_id = self.room_id
                DataBase.replaceValue(self, 'roomID', self.player.room_id)
                TeamMessage(self.client, self.player).send()
                break