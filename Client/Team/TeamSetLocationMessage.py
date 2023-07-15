from Server.Team.TeamMessage import TeamMessage
from Utils.Reader import BSMessageReader
from database.DataBase import DataBase
from Utils.Helpers import Helpers
import json

class TeamSetLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client 

    def decode(self):
        self.read_Vint()
        self.mapa = self.read_Vint()

    def process(self):
        TeamMessage(self.client, self.player)
        for player in Helpers.rooms[self.player.room_id-1]['plrs']:
            Helpers.rooms[self.player.room_id-1]['map_id'] = self.mapa
            TeamMessage(self.client, self.player).sendWithLowID(player['id'])
            break