from Utils.Writer import Writer
from database.DataBase import DataBase
import random
class BattleResult2Message(Writer):
    def __init__(self, client, player, result):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.result = result
        self.bot1 = random.randint(0, 32)
        self.bot2 = random.randint(0, 32)
        self.bot3 = random.randint(0, 32)
        self.bot4 = random.randint(0, 32)
        self.bot5 = random.randint(0, 32)
    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        win_val = 0
        lose_val = 0
        tokenGained = 0
        tropGainded = 0
        if 0 <= brawler_trophies <= 49:
            win_val = 12
            lose_val = 0
        else:
            if 50 <= brawler_trophies <= 99:
                win_val = 18
                lose_val = -1
            if 100 <= brawler_trophies <= 199:
                win_val = 16
                lose_val = -2
            if 200 <= brawler_trophies <= 299:
                win_val = 14
                lose_val = -3
            if 300 <= brawler_trophies <= 399:
                win_val = 12
                lose_val = -4
            if 400 <= brawler_trophies <= 499:
                win_val = 12
                lose_val = -5
            if 500 <= brawler_trophies <= 599:
                win_val = 12
                lose_val = -6
            if 600 <= brawler_trophies <= 699:
                win_val = 12
                lose_val = -7
            if 700 <= brawler_trophies <= 799:
                win_val = 12
                lose_val = -8
            if 800 <= brawler_trophies <= 899:
                win_val = 11
                lose_val = -9
            if 900 <= brawler_trophies <= 999:
                win_val = 10
                lose_val = -10
            if 1000 <= brawler_trophies <= 1099:
                win_val = 9
                lose_val = -11
            if 1100 <= brawler_trophies <= 1199:
                win_val = 8
                lose_val = -12
            if brawler_trophies >= 1200:
                win_val = 8
                lose_val = -12
        if self.player.battle_result == 1:
            tropGainded = lose_val
            tokenGained = 0
        elif self.player.battle_result == 0:
            tropGainded = win_val
            tokenGained = random.randint(10,50)
        self.writeVint(1) # Battle End Game Mode 
        self.writeVint(self.player.battle_result) # Result 
        self.writeVint(tokenGained) # Tokens Gained
        if tropGainded >= 0:
            if self.player.vip == 1:
                tropGainded += 8
                self.writeVint(tropGainded) # Trophies Result
            else:
                self.writeVint(tropGainded) # Trophies Result
        if tropGainded < 0:
            self.writeVint(-65 - (tropGainded)) # Trophies Result
        self.writeVint(0) # Unknown (Power Play Related)
        if self.player.vip == 1:
            self.writeVint(32) # Doubled Tokens
            tokenGained += 32
        else:
            self.writeVint(0) # Doubled Tokens
        self.writeVint(0) # Double Token Event
        self.writeVint(0) # Token Doubler Remaining
        self.writeVint(0) # Big Game/Robo Rumble Time
        self.writeVint(0) # Unknown (Championship Related)
        self.writeVint(0) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Points, 1 = Star Tokens)
        self.writeVint(0) # Challenge Reward Ammount
        self.writeVint(0) # Championship Losses Left
        self.writeVint(0) # Championship Maximun Losses
        self.writeVint(0) # Coin Shower Event
        if tropGainded > 0:
            if self.player.vip == 1:
                self.writeVint(8) # Underdog Trophies
            else:
                self.writeVint(0) # Underdog Trophies
        else:
            self.writeVint(0) # Underdog Trophies
        self.writeVint(16)# 48-спектатор 32-дружеская 16-обычная победа (-16) - повер плей
        self.writeVint(-64) # Championship Challenge Type
        self.writeVint(0) # Championship Cleared and Beta Quests
            
        # Players Array
        self.writeVint(6) # Battle End Screen Players
        
        self.writeVint(1) # Team and Star Player Type
        self.writeScId(16, self.player.brawler_id) # Player Brawler
        self.writeScId(29, self.player.skin_id) # Player Skin
        self.writeVint(self.player.brawlers_trophies[str(self.player.brawler_id)]) # Your Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(self.player.brawlerPowerLevel[str(self.player.brawler_id)]) # Your Brawler Power Level
        self.writeBoolean(True) # HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(self.player.low_id) # LowID
        self.writeString(self.player.name) # Your Name
        self.writeVint(100) # Player Experience Level
        self.writeVint(28000000 + self.player.profile_icon) # Player Profile Icon
        self.writeVint(43000000 + self.player.name_color) # Player Name Color
        if self.player.vip == 1:
            self.writeVint(43000000 + self.player.name_color) # Player Name Color
        else:
            self.writeVint(0) # Player Name Color
            
        self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.bot1) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 1 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(43000000) # Player Name Color
            
        self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, self.bot2) # Bot 2 Brawler
        self.writeVint(0) # Bot 2 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 2 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(43000000) # Player Name Color

        self.writeVint(2) # Team and Star Player Type
        self.writeScId(16, self.bot3) # Bot 3 Brawler
        self.writeVint(0) # Bot 3 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 3 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(43000000) # Player Name Color

        self.writeVint(2) # Team and Star Player Type
        self.writeScId(16, self.bot4) # Bot 4 Brawler
        self.writeVint(0) # Bot 4 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 4 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(43000000) # Player Name Color

        self.writeVint(2) # Team and Star Player Type
        self.writeScId(16, self.bot5) # Bot 5 Brawler
        self.writeVint(0) # Bot 5 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 5 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
        self.writeVint(43000000) # Player Name Color
        self.writeVint(43000000) # Player Name Color
        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(0) # Normal Experience Gained
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVint(0) # Count

        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Trophies Bar Milestone ID
        self.writeVint(self.player.brawlers_trophies[str(self.player.brawler_id)]) # Brawler Trophies
        self.writeVint(self.player.brawlers_trophies[str(self.player.brawler_id)]) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(10) # Player Experience
        self.writeVint(0) # Player Experience for Level
        
        self.writeScId(28, 0)  # Player Profile Icon (Unused since 2017)
        self.writeBoolean(False)  # Play Again
        if self.player.name != "VBC26":
            self.player.bet = tropGainded
            self.player.brawlers_trophies[str(self.player.brawler_id)] += self.player.bet
            DataBase.replaceValue(self, 'brawlersTrophies', self.player.brawlers_trophies)
            self.player.BPTOKEN = self.player.BPTOKEN + tokenGained
            DataBase.replaceValue(self, 'BPTOKEN', self.player.BPTOKEN)
            self.player.trioWINS = self.player.trioWINS + 1
            DataBase.replaceValue(self, 'trioWINS', self.player.trioWINS)
            self.player.player_experience += 10
            DataBase.replaceValue(self, 'playerExp', self.player.player_experience)