from Utils.Writer import Writer
from database.DataBase import DataBase
from Logic.Player import Players
from Utils.Helpers import Helpers

class TeamLeaveOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24125
        self.player = player

    def encode(self):
        self.writeHexa('''00000000''')
        for player in Helpers.rooms[self.player.room_id-1]['plrs']:
            if player['id'] == self.player.low_id:
                Helpers.rooms[self.player.room_id-1]['plrs'].remove(player)
                self.player.room_id = 0
                DataBase.replaceValue(self, 'roomID', self.player.room_id)