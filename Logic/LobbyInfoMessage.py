from Utils.Writer import Writer
from datetime import datetime
import random
class LobbyInfoMessage(Writer):
    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        now = datetime.now()
        ping = random.randint(19,33)
        self.writeVint(0)#\nPlayer Online: {self.count}
        self.writeString(f'NO')
        self.writeVint(0)