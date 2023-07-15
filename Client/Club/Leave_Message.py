from database.DataBase import DataBase
from Server.Club.MyAllianceMessage import MyAllianceMessage
from Server.Club.AllianceLeaveOkMessage import AllianceLeaveOkMessage
from Server.Club.AllianceChatServer import AllianceChatServer
from Server.Club.AllianceDataMessage import AllianceDataMessage

from Utils.Reader import BSMessageReader


class Leave_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):

        # Removing member 
        DataBase.loadClub(self, self.player.club_low_id)

        if self.clubmembercount == 1:
            DataBase.AddMember(self, self.player.club_low_id, self.player.low_id, self.player.name, 0)
        else:
            DataBase.AddMember(self, self.player.club_low_id, self.player.low_id, self.player.name, 2)
            DataBase.Addmsg(self, self.player.club_low_id, 4, 0, self.player.low_id, self.player.name, self.player.club_role, 4)
        # Info
        
        AllianceLeaveOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, 0).send()
        for player in self.plrids:
            if player != self.player.low_id:
                AllianceDataMessage(self.client, self.player, 0, self.player.club_low_id).sendWithLowID(player)
                AllianceChatServer(self.client, self.player, 4, self.player.club_low_id).sendWithLowID(player)

        DataBase.replaceValue(self, 'clubID', 0)
        self.player.club_low_id = 0
        DataBase.replaceValue(self, 'clubRole', 0)
        self.player.club_role = 0