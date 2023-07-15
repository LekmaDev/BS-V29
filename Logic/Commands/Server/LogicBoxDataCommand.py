from database.DataBase import DataBase
import random
from Utils.Writer import Writer


class LogicBoxDataCommand(Writer):

    def __init__(self, client, player, boxid):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxid = boxid
        self.brawler = 0
        self.randomBS = 0
        self.randomBS2 = 0
        self.reward = 3
        self.gold = 0
        self.gems = 0


    def encode(self):
        print("server")
        drop = random.randint(0,4)
        self.reward = random.choice([2,3,4,3,3,2,4])
        braler_id = None
        if drop == 1:
            numbers = random.choice(range(1, 39))
            if numbers in [33,37,35]:
                numbers = random.choice(range(1, 39))
            if numbers in [33,37,35]:
                braler_id = 1
            if braler_id is not None and self.player.UnlockedBrawlers.get(str(braler_id)) == 0:
                self.brawler = braler_id
                self.reward = 2
                self.player.UnlockedBrawlers[str(braler_id)] = 1
                DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        unlocked_brawlers = [brawler for brawler, unlocked in self.player.UnlockedBrawlers.items() if unlocked]
        if unlocked_brawlers:
            self.randomBS = random.choice(unlocked_brawlers)
            self.randomBS2 = random.choice(unlocked_brawlers)
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
            self.gold=random.randint(10,200)
            self.writeVint(self.gold) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.writeVint(1)  # Reward amount
            self.writeScId(16, int(self.brawler))  # CsvID
            self.writeVint(1)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.gold += self.gold
            DataBase.replaceValue(self, 'gold', self.player.gold)
        if self.reward == 3:
            self.gold=random.randint(10,200)
            blat1 = random.randint(10,100)
            self.writeVint(blat1)  # Reward amount
            self.writeScId(16, int(self.randomBS))  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
			
            blat2 = random.randint(10,100)
            self.writeVint(blat2)  # Reward amount
            self.writeScId(16, int(self.randomBS2))  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
			
            self.writeVint(self.gold) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.gold += self.gold
            DataBase.replaceValue(self, 'gold', self.player.gold)
        if self.reward == 4:
            self.gold=random.randint(10,200)
            self.gems=random.randint(1,12)
            blat1 = random.randint(10,100)
            self.writeVint(blat1)  # Reward amount
            self.writeScId(16, int(self.randomBS))  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.randomBS)] += blat1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
			
            blat2 = random.randint(10,100)
            self.writeVint(blat2)  # Reward amount
            self.writeScId(16, int(self.randomBS2))  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.randomBS2)] += blat2
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
			
            self.writeVint(self.gold) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
			
            self.writeVint(self.gems) # Reward ammount
            self.writeScId(0, 8) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.gold += self.gold
            DataBase.replaceValue(self, 'gold', self.player.gold)
            self.gems += self.gems
            DataBase.replaceValue(self, 'gems', self.player.gems)
        # Box end
        for i in range(13):
            self.writeVint(0)