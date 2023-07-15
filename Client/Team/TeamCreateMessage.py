from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
import random
from Utils.Reader import BSMessageReader
from Utils.Gameroom import Gameroom
from Utils.Helpers import Helpers
class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.mapSlot = self.read_Vint()
        self.map_id = self.read_Vint()
        self.roomType = self.read_Vint()

    def process(self):
        self.player.room_id = 1+len(Helpers.rooms)
        Gameroom.create(self, self.roomType, 14)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)
        TeamMessage(self.client, self.player).send()