from Utils.Writer import Writer
from database.DataBase import DataBase
import json

class PlayerProfileMessage(Writer):

    def __init__(self, client, player, high_id, low_id, players):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.high_id = high_id
        self.low_id = low_id
        self.players = players

    def encode(self):
        player = self.players
        brawlerData = json.loads(player[13])
        self.writeVint(0)  # High Id
        self.writeVint(self.low_id)  # Low Id
        self.writeVint(0)  # Unknown
        count = 0
        for brawler, unlocked in brawlerData["UnlockedBrawlers"].items():
            if unlocked:
                count += 1
       
        self.writeVint(count)  # Brawlers array
        for brawler, unlocked in brawlerData["UnlockedBrawlers"].items():
            if unlocked:
                self.writeScId(16, int(brawler))
                self.writeVint(0)
                self.writeVint(int(brawlerData["brawlersTrophies"][str(brawler)]))  # Trophies for rank
                self.writeVint(int(brawlerData["brawlersTrophies"][str(brawler)]))  # Trophies
                self.writeVint(0)  # power lvl

        self.writeVint(15)

        self.writeVint(1)
        self.writeVint(player[24])  # 3v3 victories

        self.writeVint(2)
        self.writeVint(player[21])  # Player experience

        self.writeVint(3)
        self.writeVint(player[3])  # Trophies

        self.writeVint(4)
        self.writeVint(brawlerData['highest_trophies'])  # Highest trophies

        self.writeVint(5)
        self.writeVint(count)  # Brawlers list

        self.writeVint(7)
        self.writeVint(28000000 + player[9])  # Profile icon??

        self.writeVint(8)
        self.writeVint(player[25])  # Solo victories

        self.writeVint(9)
        self.writeVint(0)  # 794 robo rumble

        self.writeVint(10)
        self.writeVint(0)  #794 big brawler

        self.writeVint(11)
        self.writeVint(0)  # Duo victories

        self.writeVint(12)
        self.writeVint(0)  # БЕЗУМИЕ 20

        self.writeVint(13)
        self.writeVint(0)  # Highest power player points

        self.writeVint(14)
        self.writeVint(0)  # Highest power play rank

        self.writeVint(15)
        self.writeVint(0)  # most challenge wins 15

        self.writeVint(16)
        self.writeVint(0) # Зомбик?? 20

        self.writeString(player[2])
        self.writeVint(100)
        self.writeVint(28000000 + player[9])  # Profile icon
        self.writeVint(43000000 + player[10])  # Name color
        if player[20] == 1:
            self.writeVint(43000000 + player[10])  # Name color
        else:
            self.writeVint(0)  # Name color
        if player[11] != 0:
            DataBase.loadClub(self, player[11])

            self.writeBoolean(True)  # Is in club

            self.writeInt(0)
            self.writeInt(player[11])
            self.writeString(self.clubName)  # club name
            self.writeVint(8)
            self.writeVint(self.clubbadgeID)  # Club badgeID
            self.writeVint(self.clubtype)  # club type | 1 = Open, 2 = invite only, 3 = closed
            self.writeVint(self.clubmembercount)  # Current members count
            self.writeVint(self.clubtrophies)
            self.writeVint(self.clubtrophiesneeded)  # Trophy required
            self.writeVint(0)  # (Unknown)
            self.writeString(self.clubregion)  # region
            self.writeVint(0)  # (Unknown)
            self.writeVint(0)  # (Unknown)
            self.writeVint(25)
            self.writeVint(player[12])
        else:
            self.writeVint(0)
            self.writeVint(0)