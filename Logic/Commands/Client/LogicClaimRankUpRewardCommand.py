from database.DataBase import DataBase
from Logic.Commands.Client.LogicClaimSL import LogicClaimSL
from Logic.Commands.Client.LogicClaimBP import LogicClaimBP
from Utils.Reader import BSMessageReader
from Utils.Writer import Writer
from Server.Login.LoginFailedMessage import LoginFailedMessage
class LogicClaimRankUpRewardCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.a = self.read_Vint()
        self.b = self.read_Vint()
        self.g = self.read_Vint()
        self.j = self.read_Vint()
        self.bp = self.read_Vint()
        self.p = self.read_Vint()
        self.k = self.read_Vint()
        self.id = self.read_Vint() # lvl id bp
        self.id2 = self.read_Vint()
    def process(self):
        DataBase.loadAccount(self)
        if self.bp == 6:
            LogicClaimSL.encode(self,self.client, self.player, self.k)
            self.player.Troproad = self.player.Troproad + 1
            DataBase.replaceValue(self, "Troproad", self.player.Troproad)
        elif self.bp == 9:
            if self.id2 in [13,18,29,39]:
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Не работает").send()
            else:
                LogicClaimBP.encode2(self,self.client, self.player, self.id, self.k, self.bp)
        elif self.bp == 10:
            if self.id2 in [11,39,54,60]:
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, "Не работает").send()
            else:
                LogicClaimBP.encode(self,self.client, self.player, self.id, self.k, self.bp)