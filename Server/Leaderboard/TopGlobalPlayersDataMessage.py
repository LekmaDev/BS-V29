from Utils.Writer import Writer
from database.DataBase import DataBase
class TopGlobalPlayersDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeBoolean(True)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        x=1
        fetch = DataBase.getLeaders(self)
        self.writeVint(len(fetch))

        for i in fetch:
            if i[0] == self.player.low_id:
                x = fetch.index(i)+1
            self.writeVint(0) # High ID
            self.writeVint(i[0]) # Low ID

            self.writeVint(1)
            self.writeVint(i[2]) # Player Trophies

            self.writeVint(1)
            self.writeString() # Club Name
            self.writeString(i[1]) # Player Name

            self.writeVint(1) # Player Level
            self.writeVint(28000000 + i[3])
            self.writeVint(43000000 + i[4])
            if i[6] == 1:
                self.writeVint(43000000 + i[4])
            else:
                self.writeVint(0)
            self.writeVint(0)


        self.writeVint(0)
        self.writeVint(x)
        self.writeVint(0)
        self.writeVint(0)

        self.writeString("BY")
