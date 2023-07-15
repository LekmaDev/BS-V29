from Server.Battle.MatchmakingInfoMessage import MatchmakingInfoMessage
from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards
from Server.Team.TeamMessage import TeamMessage
from database.DataBase import DataBase
from Utils.Gameroom import Gameroom
from Utils.Helpers import Helpers
from Server.Battle.MatchmakeCancelledMessage import MatchmakeCancelledMessage

class OnPlay(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        pass

    def process(self):
        MatchmakeCancelledMessage(self.client, self.player).send()
        self.player.room_id = 1+len(Helpers.rooms)
        self.roomType = 1
        self.map_id = 14
        Gameroom.create(self, self.roomType, self.map_id)
        DataBase.replaceValue(self, 'roomID', self.player.room_id)
        TeamMessage(self.client, self.player).send()