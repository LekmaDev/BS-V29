from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
import json

class LogicBrawlPassTokensCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        self.player.gems = self.player.gems - 30
        DataBase.replaceValue(self, 'gems', self.player.gems)
        if 0 <= self.player.BPTOKEN <= 75:
            self.player.BPTOKEN = self.player.BPTOKEN + 75
        elif 75 < self.player.BPTOKEN <= 150:
            self.player.BPTOKEN = self.player.BPTOKEN + 100
        elif 150 < self.player.BPTOKEN <= 250:
            self.player.BPTOKEN = self.player.BPTOKEN + 150
        elif 250 < self.player.BPTOKEN <= 400:
            self.player.BPTOKEN = self.player.BPTOKEN + 200
        elif 250 < self.player.BPTOKEN <= 600:
            self.player.BPTOKEN = self.player.BPTOKEN + 300
        elif 600 < self.player.BPTOKEN <= 900:
            self.player.BPTOKEN = self.player.BPTOKEN + 300
        elif 250 < self.player.BPTOKEN >= 900:
            self.player.BPTOKEN = self.player.BPTOKEN + 400
        elif self.player.BPTOKEN >= 6500:
            self.player.BPTOKEN = self.player.BPTOKEN + 500
        elif self.player.BPTOKEN >= 16500:
            self.player.BPTOKEN = self.player.BPTOKEN + 550
        elif self.player.BPTOKEN >= 19300:
            self.player.BPTOKEN = self.player.BPTOKEN + 600
        elif self.player.BPTOKEN >= 25850:
            self.player.BPTOKEN = self.player.BPTOKEN + 650
        DataBase.replaceValue(self, 'BPTOKEN', self.player.BPTOKEN)