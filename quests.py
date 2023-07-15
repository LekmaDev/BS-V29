import sqlite3
import random
import json

class auto_quests():
    def generator():
        conn = sqlite3.connect("database/Player/plr.db")
        cursor = conn.cursor()
        cursor.execute("SELECT lowID, brawlerData, trophies FROM plrs")
        player_data = cursor.fetchall()

        for player in player_data:
            lowID = player[0]
            data = json.loads(player[1])
            unlocked = [int(key) for key, value in data['UnlockedBrawlers'].items() if value == 1]
            unlocked_brawlers = random.choice([unlocked])
            quests = []

            trophies = player[2]

            if trophies < 300:
                continue

            cursor.execute("SELECT quests FROM plrs WHERE lowID = ?", (lowID,))
            current_quests = json.loads(cursor.fetchone()[0])
            if len(current_quests) >= 18:
                current_quests = []
                cursor.execute("UPDATE plrs SET quests = ? WHERE lowID = ?", (json.dumps(current_quests), lowID))
                conn.commit()

            for i in range(6):
                brawler_id = random.choice(unlocked_brawlers)
                win_count = random.randint(3, 8)
                prize = random.choice([100, 200, 400, 500, 550])
                gm = random.choice([0, 6, 3])
                quest = {"id": brawler_id,"win_count": win_count, "counts": 0, "prize": prize,"GM": gm}
                quests.append(quest)
            current_quests.extend(quests)
            cursor.execute("UPDATE plrs SET quests = ? WHERE lowID = ?", (json.dumps(current_quests), lowID))
            conn.commit()
        conn.close()

    def trop(self, ID):
        conn = sqlite3.connect("database/Player/plr.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT lowID, brawlerData, trophies FROM plrs WHERE lowID = ?", (ID,))
        player_data = cursor.fetchone()
        
        if player_data is None:
            conn.close()
            return
        
        lowID = player_data[0]
        data = json.loads(player_data[1])
        unlocked = [int(key) for key, value in data['UnlockedBrawlers'].items() if value == 1]
        unlocked_brawlers = random.choice([unlocked])
        quests = []

        trophies = player_data[2]

        if trophies < 300:
            conn.close()
            return

        cursor.execute("SELECT quests FROM plrs WHERE lowID = ?", (lowID,))
        current_quests = json.loads(cursor.fetchone()[0])
        
        if len(current_quests) >= 18:
            current_quests = []
            cursor.execute("UPDATE plrs SET quests = ? WHERE lowID = ?", (json.dumps(current_quests), lowID))
            conn.commit()

        for i in range(6):
            brawler_id = random.choice(unlocked_brawlers)
            win_count = random.randint(3, 8)
            prize = random.choice([100, 200, 400, 500, 550])
            gm = random.choice([0, 6, 3])
            quest = {"id": brawler_id,"win_count": win_count, "counts": 0, "prize": prize, "GM": gm}
            quests.append(quest)
            
        current_quests.extend(quests)
        cursor.execute("UPDATE plrs SET quests = ? WHERE lowID = ?", (json.dumps(current_quests), lowID))
        conn.commit()
        
        conn.close()