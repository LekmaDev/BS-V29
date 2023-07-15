from Utils.Writer import Writer
class AllianceRoleChangedOK(Writer):

    def __init__(self, client, player, type):
        super().__init__(client)
        self.id = 24333
        self.player = player
        self.type = type

    def encode(self):
        if self.type == 0:
            self.writeVint(81)# Event type
        elif self.type == 1:
            self.writeVint(82)