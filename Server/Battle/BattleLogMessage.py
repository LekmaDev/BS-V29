from Utils.Writer import Writer


class BattleLogMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23458
        self.player = player

    def encode(self):
        self.writeBoolean(True)
        self.writeVint(0) # Coun
