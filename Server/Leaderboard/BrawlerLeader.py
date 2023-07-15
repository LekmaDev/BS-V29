from Utils.Writer import Writer
from database.DataBase import DataBase
import sqlite3 as sql
import json
class BrawlerLeader(Writer):
    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.brawler = ID
    def by_tr(self,plr):
        return json.loads(plr[2])['brawlersTrophies'][str(self.brawler)]
    def encode(self):
        self.indexOfPlayer = 1
        self.writeVint(0)
        self.writeVint(0)
        self.writeScId(16, self.brawler)
        self.writeString()
        fetch = DataBase.GetLeaderboardByBrawler(self, self.brawler)
        fetch.sort(key=self.by_tr, reverse=True)
        x=1
        y = 0
        for i in fetch:
            if json.loads(i[2])['brawlersTrophies'][str(self.brawler)] > 0:
                y += 1
        self.writeVint(y)# Players Count

        for i in fetch:
            if json.loads(i[2])['brawlersTrophies'][str(self.brawler)] > 0:
                self.writeVint(0) # High ID
                self.writeVint(i[0]) # Low ID
                self.writeVint(1)
			
                self.writeVint(json.loads(i[2])['brawlersTrophies'][str(self.brawler)]) # Player Trophies
                self.writeVint(1)

                self.writeString() # Club Name
                self.writeString(i[1]) # Player Name

                self.writeVint(100) # Player Level
                self.writeVint(28000000 + i[3])
                self.writeVint(43000000 + i[4])
                if i[5] == 1:
                    self.writeVint(43000000 + i[4])
                else:
                    self.writeVint(0)
                self.writeVint(0)


        self.writeVint(0)
        self.writeVint(x)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("BY")
