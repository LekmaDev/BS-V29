from Utils.Writer import Writer
#from Logic.PlayerSession import PlayerSession
from Server.Battle.UDPConnectionInfo import UDPConnectionInfo
#from Utils.MatchmakingLogic import MatchmakingLogic

class MatchmakingInfoMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20405
        self.player = player

    def encode(self):
        #matchmaker = MatchmakingLogic()
        #my_battle = matchmaker.get_battle_for_id(self.player.battleID)
        self.writeInt(0)#Second
        self.writeInt(1)#len(my_battle["players"]))#Found
        self.writeInt(6)#MatchmakingLogic.MaxPlayer)#Max
        self.writeInt(0)
        self.writeInt(0)
        self.writeBoolean(True)#ShowTips
        #if len(my_battle["players"]) == MatchmakingLogic.MaxPlayer:
        #    self.player.inmm = False
        #    my_battle["battleStart"] = True
        #    my_battle["GameObjeckCount"] = len(my_battle["players"])
        #    UDPConnectionInfo(self.client, self.player).send()
        #    battle = PlayerSession(self.client, self.player)
        #    battle.start()