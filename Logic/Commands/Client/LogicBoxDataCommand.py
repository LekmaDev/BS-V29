from database.DataBase import DataBase
import random
from Utils.Writer import Writer


class LogicBoxDataCommand(Writer):

    def __init__(self, client, player, sho=0, bp=0,ids=0,boxid=0):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxid = boxid
        self.brawler = 0
        self.randomBS = 0
        self.randomBS2 = 0
        self.reward = 0
        self.gold = 0
        self.gems = 0
        self.sho = sho
        self.bp = bp
        self.ids = ids


    def encode(self):
        self.reward = random.choice([2,3,4,3,4,3,4,2,3,4])#
        unlocked_brawlers = [brawler for brawler, unlocked in self.player.UnlockedBrawlers.items() if unlocked]
        if unlocked_brawlers:
            random_bs = random.sample(unlocked_brawlers, k=2)
            self.randomBS = random_bs[0]
            self.randomBS2 = random_bs[1]
        if self.reward == 2:
            if self.brawler in [37,35,36,38,39]:
                self.reward = 3
            else:
                for id, unlocked in self.player.UnlockedBrawlers.items():
                    if unlocked == 0:
                        self.brawler = int(id)
                        break
                if self.brawler is not None:
                    if self.brawler == 0:
                        self.reward = 3
                    else:
                        self.brawler = self.brawler
                        self.player.UnlockedBrawlers[str(self.brawler)] = 1
                        DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        if self.boxid == 6:
            self.boxid = 10
        elif self.boxid == 7:
            self.boxid = 12
        elif self.boxid == 8: 
            self.boxid = 11
        elif self.boxid == 5:  # Brawl Box
            self.player.box = self.player.box - 100
            DataBase.replaceValue(self, 'box', self.player.box)
            self.boxid = 10
        elif self.boxid == 4:  # Big Box
            self.player.bigbox = self.player.box - 10
            DataBase.replaceValue(self, 'bigbox', self.player.bigbox)
            self.boxid = 12
        elif self.boxid == 3:  # Shop Box
            self.player.gems = self.player.gems - 80
            DataBase.replaceValue(self, 'gems', self.player.gems)
            self.boxid = 11
        elif self.boxid == 1:  # Shop Big Box
            self.player.gems = self.player.gems - 30
            DataBase.replaceValue(self, 'gems', self.player.gems)
            self.boxid = 12
        elif self.boxid == 4:  # Shop Mega Box
            self.player.gems = self.player.gems - 80
            DataBase.replaceValue(self, 'gems', self.player.gems)
            self.boxid = 11
        if self.reward == 2:
            self.gold=random.randint(10,200)
            self.gold += self.gold
            self.brawler = self.brawler
            DataBase.replaceValue(self, 'gold', self.player.gold)
        if self.reward == 3:
            blat2 = random.randint(10,100)
            blat1 = random.randint(10,100)
            self.gold = random.randint(1,178)
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.gold += self.gold
            DataBase.replaceValue(self, 'gold', self.player.gold)
        if self.reward == 4:
            blat2 = random.randint(10,100)
            blat1 = random.randint(10,100)
            self.gems = random.randint(1,12)
            self.gold = random.randint(1,178)
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            self.player.gold += self.gold
            self.brawler = self.brawler
            DataBase.replaceValue(self, 'gold', self.player.gold)
            self.player.gems += self.gems
            DataBase.replaceValue(self, 'gems', self.player.gems)
        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)   # Unknown
        self.writeVint(self.boxid)  # BoxID
        # Box info end

        # Reward start
        self.writeVint(self.reward) # Reward count

        # Brawler start
        if self.reward == 2:
            self.writeVint(self.gold) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) # ????
            # Brawler start
            self.writeVint(1)# Reward amount
            self.writeScId(16, int(self.brawler))  # CsvID 16
            self.writeVint(1) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
            # Brawler end
            self.player.UnlockedBrawlers[str(self.brawler)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        if self.reward == 3:
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
            self.writeVint(0) # ????
            # Brawler start
        if self.reward == 4:
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
            self.writeVint(0) # ????
            # Brawler start
			
            self.writeVint(self.gems) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(8) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) # ????
            # Brawler start
        # Box end
        if self.sho == 1:
            self.writeBoolean(False)

            self.writeVint(6)#RewardTrackType
            self.writeVint(self.player.Troproad+1)#RewardForRank
            self.writeVint(0)

            self.writeVint(1)
        elif self.sho ==2:
            self.writeBoolean(False)

            self.writeVint(self.bp)#RewardTrackType
            self.writeVint(self.ids+2)#RewardForRank
            self.writeVint(0)

            self.writeVint(1)