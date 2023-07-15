from Utils.Writer import Writer
from database.DataBase import DataBase
import random
import json
class BattleEnd2(Writer):
    def __init__(self, client, player, my_battle):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.my_battle = my_battle
    def encode(self):
        win_val = random.randint(4,8)
        lose_val = 0
        tokenGained = 0
        tropGainded = 0
        self.writeVint(2) # Battle End Game Mode 
        self.writeVint(1) # Result 
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
        self.writeVint(2) # Battle End Screen Players
        
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
            
        self.writeVint(0) # Team and Star Player Type
        self.writeScId(16, 0) # Bot 1 Brawler
        self.writeVint(0) # Bot 1 Skin
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Unknown (Power Play Related)
        self.writeVint(1) # Brawler Power Level
        self.writeBoolean(False) # HighID and LowID Array
        self.writeString("bot") # Bot 1 Name
        self.writeVint(0) # Player Experience Level
        self.writeVint(28000000) # Player Profile Icon
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
        self.writeVint(0) # Brawler Trophies
        self.writeVint(0) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Bar Milestone ID
        self.writeVint(10) # Player Experience
        self.writeVint(0) # Player Experience for Level
        
        self.writeScId(28, 0)  # Player Profile Icon (Unused since 2017)
        self.writeBoolean(False)  # Play Again