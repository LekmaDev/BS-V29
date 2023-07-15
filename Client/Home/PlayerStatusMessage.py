from Utils.Reader import BSMessageReader
from database.DataBase import DataBase

class PlayerStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.status = self.read_Vint()

    def process(self):
        self.player.online = self.status
        DataBase.replaceValue(self, 'online', self.player.online)