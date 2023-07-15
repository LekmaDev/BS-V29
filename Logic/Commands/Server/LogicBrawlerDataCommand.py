from database.DataBase import DataBase
from Utils.Writer import Writer
import random
class LogicBrawlerDataCommand(Writer):
    def __init__(self, client, player, sho=0, ID=0):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.sho = sho
        self.brawlerID = ID

    def encode(self):
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)   # Multipler
        self.writeVint(100) # BoxID
        if self.player.UnlockedBrawlers[str(self.brawlerID)] == 0:
            self.writeVint(1)#count
            self.writeVint(1)  # Reward amount
            self.player.UnlockedBrawlers[str(self.brawlerID)] = 1
            self.writeScId(16, self.brawlerID)  # CsvID
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
            self.writeVint(1)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.writeVint(self.player.Troproad)
        elif self.player.UnlockedBrawlers[str(self.brawlerID)] == 1:
            unlocked_brawlers = [brawler for brawler, unlocked in self.player.UnlockedBrawlers.items() if unlocked]
            if unlocked_brawlers:
                random_bs = random.sample(unlocked_brawlers, k=2)
                self.randomBS = random_bs[0]
                self.randomBS2 = random_bs[1]
            blat2 = random.randint(10,100)
            blat1 = random.randint(10,100)
            self.gold = random.randint(1,178)
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.gold += self.gold
            DataBase.replaceValue(self, 'gold', self.player.gold)
            self.writeVint(3)#count
            # Upgrade points start
            self.writeVint(blat1) # Reward amount
            self.writeScId(16, int(self.randomBS)) # CsvID 16
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
			#new
            self.writeVint(blat2) # Reward amount
            self.writeScId(16, int(self.randomBS2)) # CsvID 16
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
            # Upgrade points end
			
            self.writeVint(self.gold) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            # Brawler start
        if self.sho == 1:
            self.writeBoolean(False)
            self.writeVint(6)#RewardTrackType
            self.writeVint(self.player.Troproad+1)#RewardForRank
            self.writeVint(0)
            self.writeVint(1)