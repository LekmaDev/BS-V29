from Server.Club.AllianceRoleChangedOK import AllianceRoleChangedOK
from Server.Club.MyAllianceMessage import MyAllianceMessage
from database.DataBase import *
from Utils.Reader import BSMessageReader

class Promote_Alliance_Member(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.TargetHighID = self.read_int()
        self.TargetLowID = self.read_int()
        self.TargetedRole = self.read_Vint()

    def process(self):
        # Sending confirmation and updated data
        account = DataBase.loadbyID(self, self.TargetLowID)
        role = account[12]
        if self.player.club_role in [0, 1]:
            return
        if self.TargetedRole > role:
            AllianceRoleChangedOK(self.client, self.player, 0).send()
        else:
            AllianceRoleChangedOK(self.client, self.player, 1).send()
        DataBase.replaceOtherValue(self, self.TargetLowID, 'clubRole', self.TargetedRole)
        account = DataBase.loadbyID(self, self.TargetLowID)
        if self.player.club_role == 2 and account[12] ==2:
            DataBase.replaceValue(self, "clubRole", 4)
    		        	
        MyAllianceMessage(self.client, self.player, self.player.club_low_id).send()