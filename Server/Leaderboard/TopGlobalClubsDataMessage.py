from Utils.Writer import Writer
from database.DataBase import DataBase

class TopGlobalClubsDataMessage(Writer):

    def __init__(self, client, player, type):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.type = type

    def encode(self):
        self.writeVint(2)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        x=1
        DataBase.LeaderClub(self)
        self.writeVint(self.AllianceCount) # Players Count
        for i in self.club_list:
            DataBase.loadClub(self, i)
            self.writeVint(0) # Club High ID
            self.writeVint(i) # Club Low ID

            self.writeVint(1)
            self.writeVint(self.clubtrophies) # Club Trophies
            self.writeVint(2)

            self.writeString(self.clubName) # Club Name
            self.writeVint(self.clubmembercount) # Club Members Count

            self.writeVint(8) # Club Badge
            self.writeVint(self.clubbadgeID) # Club Name Color
            x += 1

        self.writeVint(0)
        self.writeVint(x) # Index of the club
        self.writeVint(0)
        self.writeVint(0)
        self.writeString("BY")