import json, random
from database.DataBase import database
import sqlite3
class Quest:
    def EncodeQuest(self):
        self.writeBoolean(True) # Quests Boolean
        questsCount = 0
        if self.player.trophies > 299:
            conn = sqlite3.connect('database/Player/plr.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.player.low_id,))
            user = cursor.fetchone()
            quests2 = user[29]
            quests = json.loads(quests2)
            questsCount = 0
            for i in quests:
                questsCount += 1
        
        if questsCount > 99:
            for item in quests:
                self.writeVint(questsCount)
                self.writeVint(0)
                self.writeVint(0)
                self.writeVint(1) # Mission Type
                self.writeVint(item['counts']) # Current Quest Goal
                self.writeVint(item['win_count']) # Max Quest Goal
                self.writeVint(item['prize']) # Tokens Reward
                self.writeVint(0)
                self.writeVint(0) # Current Level 
                self.writeVint(0) # Max Level
                self.writeVint(0) # Quest Type | 0 = Season Quest, 1 = Daily Quest
                self.writeBoolean(False) # Brawl Pass Exclusive
                self.writeScId(16, item['id']) # Brawler ID
                self.writeVint(0) # Gamemode ID
                self.writeVint(0)
        else:
            self.writeVint(0)