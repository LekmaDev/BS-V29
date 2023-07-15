from Utils.Reader import BSMessageReader
from Logic.Commands.Client.LogicPurchaseBoxCommand import LogicPurchaseBoxCommand
from Logic.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Logic.Commands.Client.LogicUpgradeBrawler import Upgrade_Brawler
from Logic.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Logic.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Logic.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Logic.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Logic.Commands.Client.LogicClaimRankUpRewardCommand import LogicClaimRankUpRewardCommand
from Logic.Commands.Client.LogicBuyBrawlPassCommand import LogicBuyBrawlPassCommand
from Logic.Commands.Client.LogicBrawlPassTokensCommand import LogicBrawlPassTokensCommand
class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.a = self.read_Vint()
        self.b = self.read_Vint()
        self.c = self.read_Vint()
        self.d = self.read_Vint()
        self.commandID = self.read_Vint()


    def process(self):
        if self.commandID == 500 or self.commandID == 535:
            LogicPurchaseBoxCommand.decode(self)
            LogicPurchaseBoxCommand.process(self)
        elif self.commandID == 517:
            LogicClaimRankUpRewardCommand.decode(self)
            LogicClaimRankUpRewardCommand.process(self)
        elif self.commandID == 506:
            LogicSelectSkinCommand.decode(self)
            LogicSelectSkinCommand.process(self)
        elif self.commandID == 505:
            LogicSetPlayerThumbnailCommand.decode(self)
            LogicSetPlayerThumbnailCommand.process(self)
        elif self.commandID == 519:
            LogicPurchaseOfferCommand.decode(self)
            LogicPurchaseOfferCommand.process(self)
        elif self.commandID == 520:
            Upgrade_Brawler.decode(self)
            Upgrade_Brawler.process(self)
        elif self.commandID == 521:
            LogicPurchaseHeroLvlUpMaterialCommand.decode(self)
            LogicPurchaseHeroLvlUpMaterialCommand.process(self)
        elif self.commandID == 527:
            LogicSetPlayerNameColorCommand.decode(self)
            LogicSetPlayerNameColorCommand.process(self)
        elif self.commandID == 534:
            LogicBuyBrawlPassCommand.decode(self)
            LogicBuyBrawlPassCommand.process(self)
        elif self.commandID == 536:
            LogicBrawlPassTokensCommand.decode(self)
            LogicBrawlPassTokensCommand.process(self)