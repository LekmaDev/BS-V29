from database.DataBase import DataBase
from Server.Team.TeamMessage import TeamMessage
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
import json
class TeamMemberStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.state = self.read_Vint()
        self.player.pin = self.read_Vint()
        self.player.mode = self.read_Vint()

    def process(self):
        TeamMessage(self.client, self.player)
        for player in Helpers.rooms[self.player.room_id-1]['plrs']:
            if player['state'] == 8:
                player['state'] = 5
                TeamMessage(self.client, self.player).sendWithLowID(player['id'])
            else:
                player['state'] = self.player.state
                TeamMessage(self.client, self.player).sendWithLowID(player['id'])