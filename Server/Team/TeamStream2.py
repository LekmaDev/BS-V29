from Utils.Writer import Writer
from database.DataBase import DataBase
from Utils.Helpers import Helpers
import json
class TeamStream2(Writer):

    def __init__(self, client, player,sender,name,msg):
        super().__init__(client)
        self.id = 24131
        self.player = player
        self.sender = sender
        self.name = name
        self.msg = msg

    def encode(self):
        self.writeVint(0) # High ID
        self.writeVint(self.player.room_id) # Room ID
        self.writeVint(1) # count
        if True:
            self.writeVint(2) # Event? 
            self.writeVint(0)
            self.writeVint(Helpers.rooms[self.player.room_id-1]['Tick']+1) # Tick? 
            self.writeVint(0)  # High ID
            self.writeVint(self.sender) # Low id
            self.writeString(f"{self.name}") # Plr Name? 
            self.writeVint(0)
            self.writeVint(0) # Age Seconds (TID_STREAM_ENTRY_AGE)
            self.writeVint(0) # Boolean
            self.writeString(f"{self.msg}") # Plr msg