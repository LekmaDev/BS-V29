from Utils.Writer import Writer


class PlayAgainStatusMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24777
        self.player = player

    def encode(self):
        self.writeInt(2) # 0 = Waiting, 1 = crash ?, 2 = Matchmaking 
        self.writeInt(2) # ??
        self.writeInt(1) # ?
        self.writeInt(2) # i think it's players in again
