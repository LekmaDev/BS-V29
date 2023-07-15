from Client.Login.ClientHelloMessage import ClientHelloMessage
from Client.Login.LoginMessage import LoginMessage
from Client.KeepAliveMessage import KeepAliveMessage
from Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Client.Home.AskProfileMessage import AskProfileMessage
from Client.AnalyticsEventMessage import AnalyticsEventMessage
from Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Client.SetNameMessage import SetNameMessage
from Client.Home.GetLeaderboardMessage import GetLeaderboardMessage
from Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Client.ClientCapabilities import ClientCapabilities
from Logic.Commands.LogicCommandManager import EndClientTurn
from Client.Battle.Cancel_Matchmaking import CancelMatchMaking
from Client.Battle.OnPlay import OnPlay
#from Client.Battle.ClientInputMessage import ClientInputMessage
#from Client.Battle.ClientInfoMessage import ClientInfoMessage
from Client.Home.GoHomeMessage import GoHomeMessage


#room
from Client.Team.TeamSearch import TeamSearch
from Client.Team.TeamCreateMessage import TeamCreateMessage
from Client.Team.TeamSetLocationMessage import TeamSetLocationMessage
from Client.Team.TeamLeaveMessage import TeamLeaveMessage
from Client.Team.TeamChangeBrawlerMessage import TeamChangeBrawlerMessage
from Client.Team.TeamSpectateMessage import TeamSpectateMessage
from Client.Team.TeamChat import TeamChat
from Client.Team.TeamPremadeChatMessage import TeamPremadeChatMessage
from Client.Team.TeamInviteMessage import TeamInviteMessage
from Client.Team.TeamKick import TeamKick
from Client.Team.TeamInvitationResponseMessage import TeamInvitationResponseMessage
#club
from Client.Team.TeamMemberStatusMessage import TeamMemberStatusMessage
from Client.Club.AskForJoinableAlliancesList import AskForJoinableAlliancesList
from Client.Club.CreateAllianceMessage import CreateAllianceMessage
from Client.Club.AskForAllianceData import AskForAllianceData
from Client.Club.JoinAllianceMessage import JoinAllianceMessage
from Client.Club.AllianceStreamMessage import AllianceStreamMessage
from Client.Club.Promote_Alliance_Member import Promote_Alliance_Member
from Client.Club.SendClubFriendMessage import SendClubFriendMessage


from Client.Friend.AddFriendMessage import AddFriendMessage
from Client.Friend.AskForFriendListMessage import AskForFriendListMessage
from Client.Friend.AcceptFriendMessage import AcceptFriendMessage

from Client.Home.SetSupportedCreatorMessage import SetSupportedCreatorMessage
from Client.Battle.HomeBattleReplayMessage import HomeBattleReplayMessage
from Client.Club.Kick_Member_Message import Kick_Member_Message
from Client.Club.Leave_Message import Leave_Message
from Client.Friend.SendAllianceInvitationFriend import SendAllianceInvitationFriend
from Client.Friend.RemoveFriendMessage import RemoveFriendMessage
packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilities,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    10212: SetNameMessage,
    14102: EndClientTurn,
    14103: OnPlay,
    14101: GoHomeMessage,
    14106: CancelMatchMaking,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: AskProfileMessage,
    #10177: ClientInfoMessage,
    #10555: ClientInputMessage,


    # Friendly battle lobby
    
    14366: PlayerStatusMessage,
    14403: GetLeaderboardMessage,
    14600: AvatarNameCheckRequestMessage,

#GAMEROOM
    14199: TeamSearch,
    14350: TeamCreateMessage,
    14352: TeamKick,
    14353: TeamLeaveMessage,
    14354: TeamChangeBrawlerMessage,
    #14355: TeamSetMemberReadyMessage,
    14365: TeamInviteMessage,
    14358: TeamSpectateMessage,
    14359: TeamChat,
    14369: TeamPremadeChatMessage,
    14361: TeamMemberStatusMessage,
    14363: TeamSetLocationMessage,
    14479: TeamInvitationResponseMessage,
    14303: AskForJoinableAlliancesList,
    14301: CreateAllianceMessage,
    14302: AskForAllianceData,
    14305: JoinAllianceMessage,
    14315: AllianceStreamMessage,
    14306: Promote_Alliance_Member,
    14326: SendClubFriendMessage,
    14307: Kick_Member_Message,
    14308: Leave_Message,
#френдв
    10504: AskForFriendListMessage,
    10501: AcceptFriendMessage,
    10502: AddFriendMessage,
    10506: RemoveFriendMessage,
    14322: SendAllianceInvitationFriend,
	
    18686: SetSupportedCreatorMessage,
    14114: HomeBattleReplayMessage,
}