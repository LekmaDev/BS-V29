from Utils.Writer import Writer
from Server.Home.OwnHomeDataMessage import OwnHomeDataMessage 

class KeepAliveOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20108
        self.player = player

    def encode(self):
        pass