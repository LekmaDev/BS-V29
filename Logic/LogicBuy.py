from Utils.Writer import Writer
from random import randint as r
from database.DataBase import DataBase
class LogicBuy(Writer):

    def __init__(self, client, player, id11, id22, id33, mult11, mult22, mult33, brawler11, brawler22, brawler33, skin11, skin22, skin33):
        super().__init__(client)
        self.id = 24111
        self.player = player

        self.id1 = id11
        self.id2 = id22
        self.id3 = id33
        
        self.mult1 = mult11
        self.mult2 = mult22
        self.mult3 = mult33

        self.brawler1 = brawler11
        self.brawler2 = brawler22
        self.brawler3 = brawler33
        
        self.skin1 = skin11
        self.skin2 = skin22
        self.skin3 = skin33

    def encode(self):
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(100)
        
        if self.id1 != 0 and self.id2 != 0 and self.id3 != 0:
               self.writeVint(3) # Reward count
        elif self.id1 != 0 and self.id2 != 0:
               self.writeVint(2) # Reward count
        else:
               self.writeVint(1) # Reward count
        	
        
        if self.id1 == 1:
            self.writeVint(self.mult1) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end

            self.player.gold += self.mult1
            DataBase.replaceValue(self, 'gold', self.player.gold)
        elif self.id1 == 2: # Gems
            self.writeVint(self.mult1) # Reward ammount
            self.writeScId(0, 8) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.gems += self.mult1
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif self.id1 == 5: # Brawler
            self.writeVint(self.mult1)  # Reward amount
            self.writeScId(16, self.brawler1)  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.brawler1)] = 1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
        elif self.id1 == 6: # Brawler
            self.writeVint(self.mult1)  # Reward amount
            self.writeScId(16, self.brawler1)  # CsvID
            self.writeVint(1)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.UnlockedBrawlers[str(self.brawler1)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        elif self.id1 == 7: # Skin
            self.writeVint(1) # Value
            self.writeVint(0) # ScId
            self.writeVint(9) # Reward ID
            self.writeScId(29, self.skin1) # ScId
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)
            self.player.UnlockedSkins[str(self.skin1)] = 1
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
        if self.id2 == 1:
            self.writeVint(self.mult2) # Reward ammount
            self.writeScId(0, 8) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.gems += self.mult2
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif self.id2 == 2: # Gems
            self.writeVint(self.mult2) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end

            self.player.gold += self.mult2
            DataBase.replaceValue(self, 'gold', self.player.gold)
        elif self.id2 == 5: # Brawler
            self.writeVint(self.mult2)  # Reward amount
            self.writeScId(16, self.brawler2)  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.brawler2)] = 1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
        elif self.id2 == 6: # Brawler
            self.writeVint(self.mult2)  # Reward amount
            self.writeScId(16, self.brawler2)  # CsvID
            self.writeVint(1)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.UnlockedBrawlers[str(self.brawler2)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        elif self.id2 == 7: # Skin
            self.writeVint(1) # Value
            self.writeVint(0) # ScId
            self.writeVint(9) # Reward ID
            self.writeScId(29, self.skin2) # ScId
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)
            self.player.UnlockedSkins[str(self.skin2)] = 1
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
        if self.id3 == 1:
            self.writeVint(self.mult3) # Reward ammount
            self.writeScId(0, 7) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end

            self.player.gold += self.mult3
            DataBase.replaceValue(self, 'gold', self.player.gold)
        elif self.id3 == 2: # Gems
            self.writeVint(self.mult3) # Reward ammount
            self.writeScId(0, 8) # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.gems += self.mult3
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif self.id3 == 5: # Brawler
            self.writeVint(self.mult3)  # Reward amount
            self.writeScId(16, self.brawler3)  # CsvID
            self.writeVint(6)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.brawlerPoints[str(self.brawler3)] = 1
            DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
        elif self.id3 == 6: # Brawler
            self.writeVint(self.mult3)  # Reward amount
            self.writeScId(16, self.brawler3)  # CsvID
            self.writeVint(1)  # RewardID
            self.writeHexa('''00 00 00''')  # Reward end
            self.player.UnlockedBrawlers[str(self.brawler3)] = 1
            DataBase.replaceValue(self, 'UnlockedBrawlers', self.player.UnlockedBrawlers)
        elif self.id3 == 7: # Skin
            self.writeVint(1) # Value
            self.writeVint(0) # ScId
            self.writeVint(9) # Reward ID
            self.writeScId(29, self.skin3) # ScId
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)
            self.player.UnlockedSkins[str(self.skin3)] = 1
            DataBase.replaceValue(self, 'UnlockedSkins', self.player.UnlockedSkins)
            
        for i in range(13):
            self.writeVint(0)