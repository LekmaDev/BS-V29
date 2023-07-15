from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Server.Login.LoginFailedMessage import LoginFailedMessage

class LogicSetPlayerNameColorCommand(BSMessageReader):
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
        self.name_color = self.read_Vint()


    def process(self):
        vip = [1,2,3,4,5,6,7,8,9,10,11]
        if self.name_color in vip:
            if self.player.vip == 0:
                self.player.err_code = 1
                LoginFailedMessage(self.client, self.player, f"У вас нет вип статуса. Ваш ID: {self.player.low_id} Купить вип можно в тг:@itdlaloxov").send()
            else:
                DataBase.replaceValue(self, 'name_color', self.name_color)
        else:
            DataBase.replaceValue(self, 'name_color', self.name_color)