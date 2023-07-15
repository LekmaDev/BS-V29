from Server.Club.MyAllianceMessage import MyAllianceMessage
from Server.Club.AllianceJoinOkMessage import AllianceJoinOkMessage
from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Server.Login.LoginFailedMessage import LoginFailedMessage

class CreateAllianceMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        DataBase.CountClub(self)
        # ClubID
        self.clubHighID = 0
        self.clubLowID = 1+self.AllianceCount

        # Info
        self.clubName = self.read_string()    # Club name  
        self.clubdescription = self.read_string()    # Club description

        # Badge
        self.BadgeIdentifier = self.read_Vint()      # Badge Identifier
        self.clubbadgeID = self.read_Vint()      # BadgeID

        # Region
        self.RegionIdentifier = self.read_Vint()      # Region Identifier
        self.clubregionID = self.read_Vint()      # RegionID 

        # Settings
        self.clubtype = self.read_Vint()      # Type
        self.clubtrophiesneeded = self.read_Vint()      # Trophy required
        self.clubfriendlyfamily = self.read_Vint()      # Family friendly
    def process(self):
        self.player.club_low_id = self.clubLowID
        self.player.club_role = 2
        DataBase.replaceValue(self, 'clubID', self.player.club_low_id)
        DataBase.replaceValue(self, 'clubRole', 2)
        #create club
        DataBase.createClub(self, self.clubLowID)
        # Club data
        AllianceJoinOkMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player, self.clubLowID).send()