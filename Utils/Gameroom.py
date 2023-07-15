import random
from Utils.Helpers import Helpers
class Gameroom:
    def create(self, roomType=1, map_id=14):
        count = len(Helpers.rooms)
        new_room = {'index': count, 'roomID': self.player.room_id, 'roomType': self.roomType, 'map_id': self.map_id,'Tick': 0,'plrs': [{'id': self.player.low_id, 'isOwner': 1, 'state': 2}],'invites':[],'Premade':[], 'msg': []}
        Helpers.rooms.append(new_room)