from Utils.Writer import Writer
from database.DataBase import DataBase
from Utils.Helpers import Helpers
from Server.Team.TeamMessage import TeamMessage
import json
class TeamStream(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24131
        self.player = player

    def encode(self):
        fm = []
        self.writeVint(0)
        self.writeVint(self.player.room_id)
        self.writeVint(1)
        dataid = 0
        index = 0
        for id in Helpers.rooms:
            dataid=id['index']
            if int(Helpers.rooms[dataid]['roomID']) == self.player.room_id:
                index = dataid
        for plr in Helpers.rooms[index]['Premade']:
            if len(Helpers.rooms[index]['Premade']) > 1:
                Helpers.rooms[index]['Premade'] = []
            if plr['pin'] in fm:
                self.writeVint(6)
            else:
                self.writeVint(8)
                # StreamEntry::encode
                self.players = DataBase.loadbyID(self,plr['id'])
                self.writeVint(0)
                self.writeVint(Helpers.rooms[self.player.room_id-1]['Tick']) # tick
                self.writeVint(0)
                self.writeVint(plr['id'])
                self.writeString(f"{self.players[2]}")
                self.writeVint(0)
                self.writeVint(0) # Age Seconds (TID_STREAM_ENTRY_AGE)
                self.writeVint(0) # Boolean
                if plr['Type'] in fm:
                    self.writeScId(40, 0)
                else:
                    self.writeScId(40, plr['Type']) # Message Data ID (40 - messages.csv)
                    self.writeBoolean(True) # Target Boolean
                    self.writeString(self.player.name) # Target Name
                    self.writeVint(0) # ??
                    self.writeVint(52000000 + plr['Type'])
        TeamMessage(self.client, self.player).send()