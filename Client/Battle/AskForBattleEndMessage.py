from Server.Battle.BattleResultMessage import BattleResultMessage
from Server.Battle.BattleResult2Message import BattleResult2Message
import json
from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.battle_result = self.read_Vint()
        self.read_Vint()
        self.player.rank = self.read_Vint()
        locationID = self.read_Vint() # Locations CsvID
        self.map = self.read_Vint() # Selected Map
        self.players = self.read_Vint() # Battle End Players
    def process(self):
        #config = open('config.json', 'r')
        #content = config.read()
        #settings = json.loads(content)
        #if self.player.name in settings['DelName']:
        #    print("FUCK")
        #else:
        if self.players == 10:
            BattleResultMessage(self.client, self.player).send()
        elif self.players == 6:
            BattleResult2Message(self.client, self.player, 1).send()