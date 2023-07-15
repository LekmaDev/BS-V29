from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards

class LogicSelectSkinCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.brawler_id = self.read_Vint()


    def process(self):
        DataBase.replaceValue(self, 'skinID', self.player.skin_id)
        DataBase.replaceValue(self, 'brawlerID', self.player.brawler_id)
