from Utils.Reader import BSMessageReader
from database.DataBase import DataBase
from Server.Club.MyAllianceMessage import MyAllianceMessage
from Server.Club.AllianceChatServer import AllianceChatServer
from Server.Club.KickMemberOK import AllianceKickMemberOK


class Kick_Member_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
    def decode(self):
        self.read_int()
        self.lowID = self.read_int()
        self.reason = self.read_string()
    def process(self):
        account = DataBase.loadbyID(self, self.lowID)
        
        DataBase.AddMember(self, account[3], self.lowID, account[1], 2)
        AllianceKickMemberOK(self.client, self.player).send()
        self.clubLowID = account[3]
        i = DataBase.loadbyID(self, self.player.low_id)
        
        DataBase.replaceOtherValue(self, self.lowID, "clubID", 0)
        DataBase.replaceOtherValue(self, self.lowID, "clubRole", 0)
        DataBase.Addmsg(self, self.player.club_low_id, 4, 1, account[2], self.player.name, self.player.club_role, 1)
        
        	
        MyAllianceMessage(self.client, self.player, self.clubLowID).send()
        DataBase.loadClub(self, self.player.club_low_id)
        for i in self.plrids:
        	AllianceChatServer(self.client, self.player, "dev", self.player.club_low_id).send()