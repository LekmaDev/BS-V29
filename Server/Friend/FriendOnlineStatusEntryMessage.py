from Utils.Writer import Writer

class FriendOnlineStatusEntryMessage(Writer):

    def __init__(self, client, player, lowID, status, room_id):
        super().__init__(client)
        self.id = 24555
        self.player = player 
        self.lowID = lowID
        self.status = status
        self.room_id = room_id
    def encode(self):
        self.writeInt(0)
        self.writeInt(self.lowID)#лов ид
        self.writeBoolean(True)
        self.writeInt(0)
        self.writeInt(self.lowID)#лов ид
        self.writeVint(self.status)#стаиус
        self.writeVint(0)#если вверху 0 то тут ставь 1 и будет он не в сетм
        if self.room_id > 0:
            self.writeBoolean(True)
        else:
            self.writeBoolean(False)
        self.writeBoolean(False)