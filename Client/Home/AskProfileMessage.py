from Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Utils.Reader import BSMessageReader
from database.DataBase import DataBase


class AskProfileMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.high_id = self.read_int()
        self.low_id = self.read_int()
        self.players = DataBase.loadbyID(self, self.low_id)


    def process(self):
        PlayerProfileMessage(self.client, self.player, self.high_id, self.low_id, self.players).send()
