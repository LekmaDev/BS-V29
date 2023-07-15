from Utils.Writer import Writer
from database.DataBase import DataBase
from Utils.Gameroom import Gameroom
from Utils.Helpers import Helpers
import json
from Server.Team.TeamInvitationMessage import TeamInvitationMessage

class TeamMessage(Writer):
    def __init__(self, client, player, roomType=1):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.playerCount = 0
        self.roomType = roomType
    def encode(self):
        self.writeVint(int(Helpers.rooms[self.player.room_id-1]['roomType']))
        self.writeVint(0)
        self.writeVint(3)#max plr
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeInt(self.player.room_id)
        self.writeVint(1557129593)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
		
		
        self.writeScId(15, int(Helpers.rooms[self.player.room_id-1]['map_id']))# MapID
        #playe
        for plr in Helpers.rooms[self.player.room_id-1]['plrs']:
            self.writeVint(len(Helpers.rooms[self.player.room_id-1]['plrs']))#count plrs
            self.writeVint(plr['isOwner'])  # Boolean admin
            self.players = DataBase.loadbyID(self,plr['id'])
            self.writeInt(0)#hight_id
            self.writeInt(self.players[1])#low_id
            brawler=self.players[14]
            self.writeScId(16, self.players[14])#brawler
            self.writeScId(29, self.players[15])#skin
            brawlerData = json.loads(self.players[13])
            self.writeVint(int(brawlerData["brawlersTrophies"][str(brawler)]))
            self.writeVint(int(brawlerData["brawlersTrophies"][str(brawler)]))
            self.writeVint(1) # brawler level
            self.writeVint(plr['state']) #status
            self.writeVint(0) # Is ready
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeString(f"{self.players[2]}")
            self.writeVint(100)
            self.writeVint(28000000 + self.players[9])
            self.writeVint(43000000 + self.players[10])
            if self.players[20] == 1:
                self.writeVint(43000000 + self.players[10])
            else:
                self.writeVint(0)
            self.writeVint(0)#sps
            self.writeVint(0)#spg
			
        self.writeVint(len(Helpers.rooms[self.player.room_id-1]['invites']))
        if len(Helpers.rooms[self.player.room_id-1]['invites']) > 0:
            for data in Helpers.rooms[self.player.room_id-1]['invites']:
                if data['state'] == 0:
                    TeamInvitationMessage(self.client, self.player, self.player.room_id, self.player.low_id).sendWithLowID(data['id'])
                    self.writeVint(1)
                    self.writeInt(0)
                    self.writeInt(self.player.room_id)
                    self.writeInt(0)
                    self.writeInt(data['id'])#low_id
                    self.invtitesload = DataBase.loadbyID(self,data['id'])
                    self.writeString(f"{self.invtitesload[2]}")
                    self.writeVint(0)#1
                    self.writeVint(data['slot'])#slot
		
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(6)