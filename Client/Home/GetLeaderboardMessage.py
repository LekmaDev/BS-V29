from Server.Leaderboard.TopGlobalPlayersDataMessage import TopGlobalPlayersDataMessage
from Server.Leaderboard.BrawlerLeader import BrawlerLeader
from Server.Leaderboard.TopGlobalClubsDataMessage import TopGlobalClubsDataMessage
from Utils.Reader import BSMessageReader
from database.DataBase import DataBase
class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.is_local = self.read_Vint()
        self.type = self.read_Vint()
        self.read_Vint()

    def process(self):
	#0 boew 1 Global top 2 Club
        if self.type == 0:
            if self.is_local == 1 or self.type == 0:
                BrawlerLeader(self.client, self.player, self.read_Vint()).send()
            else:
                BrawlerLeader(self.client, self.player, self.read_Vint()).send()
        if self.type == 1:
            if self.is_local == 1 or self.type == 0:
                TopGlobalPlayersDataMessage(self.client, self.player).send()
            else:
                TopGlobalPlayersDataMessage(self.client, self.player).send()
        if self.type == 2:
            if self.is_local == 1 or self.type == 0:
                TopGlobalClubsDataMessage(self.client, self.player, 2).send()
            else:
                TopGlobalClubsDataMessage(self.client, self.player, 2).send()