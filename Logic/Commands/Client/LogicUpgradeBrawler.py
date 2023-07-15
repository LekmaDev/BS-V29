from database.DataBase import DataBase
from Utils.Reader import BSMessageReader

class Upgrade_Brawler(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()                  # csvID
        self.BrawlerID = self.read_Vint() # BrawlerID


    def process(self):
        self.player.brawlerPowerLevel[str(self.BrawlerID)] += 1
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 1:
            newGold = self.player.gold - 20
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 2:
            newGold = self.player.gold - 35
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 3:
            newGold = self.player.gold - 75
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 4:
            newGold = self.player.gold - 140
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 5:
            newGold = self.player.gold - 290
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 6:
            newGold = self.player.gold - 480
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 7:
            newGold = self.player.gold - 800
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        if self.player.brawlerPowerLevel[str(self.BrawlerID)] == 8:
            newGold = self.player.gold - 1250
            self.player.gold = newGold
            DataBase.replaceValue(self, 'gold', newGold)
        DataBase.replaceValue(self, 'brawlerPowerLevel', self.player.brawlerPowerLevel)