from Utils.Writer import Writer
from database.DataBase import DataBase

class LogicSetSupportedCreatorCommand(Writer):

    def __init__(self, client, player, state):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.state = state

    def encode(self):
        self.writeVint(1)
        self.writeString(self.player.ccc)
        self.writeVint(1)
