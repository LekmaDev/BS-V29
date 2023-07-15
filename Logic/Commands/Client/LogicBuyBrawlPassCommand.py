from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
import json
class LogicBuyBrawlPassCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
        config["buybp"].append(self.player.low_id)
        newGems = self.player.gems - 169
        DataBase.replaceValue(self, 'gems', newGems)
        with open("config.json", "w", encoding='utf-8') as f:
                json.dump(config, f, indent=4)