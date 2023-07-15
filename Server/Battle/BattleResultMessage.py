from Utils.Writer import Writer
from database.DataBase import DataBase
import random
import json
import sqlite3
class BattleResultMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player
        self.bot1 = random.randint(0, 32)
        self.bot2 = random.randint(0, 32)
        self.bot3 = random.randint(0, 32)
        self.bot4 = random.randint(0, 32)
        self.bot5 = random.randint(0, 32)
    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.brawler_id)]
        tropGainded = 0
        tokenGained = 0
		
        rank_1_val = 12
        rank_2_val = 11
        rank_3_val = 10
        rank_4_val = 9
        rank_5_val = 8
        rank_6_val = 7
        rank_7_val = -2
        rank_8_val = -4
        rank_9_val = -8
        rank_10_val = -10
        if self.player.rank == 1:
            tropGainded = rank_1_val
            tokenGained = random.randint(10,50)
        elif self.player.rank == 2:
            tropGainded = rank_2_val
            tokenGained = random.randint(10,45)
        elif self.player.rank == 3:
            tropGainded = rank_3_val
            tokenGained = random.randint(10,40)
        elif self.player.rank == 4:
            tropGainded = rank_4_val
            tokenGained = random.randint(10,35)
        elif self.player.rank == 5:
            tropGainded = rank_5_val
            tokenGained = random.randint(10,30)
        elif self.player.rank == 6:
            tropGainded = rank_6_val
            tokenGained = random.randint(10,25)
        elif self.player.rank == 7:
            tropGainded = rank_7_val
            tokenGained = random.randint(10,20)
        elif self.player.rank == 8:
            tropGainded = rank_8_val
            tokenGained = random.randint(10,15)
        elif self.player.rank == 9:
            tropGainded = rank_9_val
            tokenGained = random.randint(1,10)
        elif self.player.rank == 10:
            tropGainded = rank_10_val
            tokenGained = random.randint(1,10)
        self.writeVint(2) # Battle End Game Mode 
        self.writeVint(self.player.rank) # Result 
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
        self.writeVint(1) # Championship Cleared and Beta Quests
            
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

        #start logic quest
        conn = sqlite3.connect('database/Player/plr.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.player.low_id,))
        user = cursor.fetchone()
        quests2 = user[29]
        quests = json.loads(quests2)
        for item in quests:
            if item['counts']+1 == item['win_count']:
                quests.remove(item)
                tokenGained += item['prize']
            else:
                if tropGainded > 0:
                    if item['id'] == self.player.brawler_id:
                        item['counts'] += 1
                else:
                    pass
        updated_quests = json.dumps(quests)
        cursor.execute('UPDATE plrs SET quests=? WHERE lowID=?', (updated_quests, self.player.low_id))
        conn.commit()
        conn.close()
        #end logic quest
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