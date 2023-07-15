from database.DataBase import DataBase
from Utils.Writer import Writer


class LogicTropRoad(Writer):

    def __init__(self, client, player, boxid=10, ammo=0, who=0, brawler=0):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxid = boxid
        self.ammo = ammo
        self.who = who
        self.brawler = brawler

    def encode(self):
        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)   # Unknown
        self.writeVint(self.boxid)  # BoxID 
        if self.boxid == 100:
            if self.who == 6:
                self.writeVint(1) # Reward amount
                self.writeVint(self.ammo) # Reward amount
                self.writeScId(16, int(self.brawler)) # CsvID 16
                self.writeVint(6) # Reward ID
                self.writeVint(0) # CsvID 29
                self.writeVint(0) # CsvID 52
                self.writeVint(0) # CsvID 23
                self.writeVint(0) 
                self.player.brawlerPoints[str(self.brawler)] += self.ammo
                DataBase.replaceValue(self, 'brawlerPoints', self.player.brawlerPoints)
            else:
                self.writeVint(1) # Reward amount
                self.writeVint(self.ammo) # Reward amount
                self.writeVint(0) # CsvID 16
                self.writeVint(7) # Reward ID
                self.writeVint(0) # CsvID 29
                self.writeVint(0) # CsvID 52
                self.writeVint(0) # CsvID 23
                self.writeVint(0) # ????
                self.player.gold = self.player.gold + self.ammo
                DataBase.replaceValue(self, "gold", self.player.gold)
        else:
            self.writeVint(1) # Reward amount
            self.writeVint(1) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(7) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) # ????
        # Box end
        self.writeBoolean(False)

        self.writeVint(6)#RewardTrackType
        self.writeVint(self.player.Troproad+1)#RewardForRank
        self.writeVint(0)

        self.writeVint(1)