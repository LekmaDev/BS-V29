from Utils.Reader import BSMessageReader
import sqlite3
import json
from Server.Friend.FriendListMessage import FriendListMessage
from database.DataBase import DataBase

class SendClubFriendMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.HighID = self.read_int()
        self.LowID = self.read_int()

    def process(self):
        conn = sqlite3.connect('database/Player/plr.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.player.low_id,))
        user = cursor.fetchone()
        friends_json = user[22]
        friends = json.loads(friends_json)
        new_friend = {'id':self.LowID,'state':2}
        friends.append(new_friend)
        friends_json = json.dumps(friends)
        cursor.execute('UPDATE plrs SET friends=? WHERE lowID=?', (friends_json, self.player.low_id))
        conn.commit()
        conn.close()
        
        
        
        conn = sqlite3.connect('database/Player/plr.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.LowID,))
        user = cursor.fetchone()
        friends_json2 = user[22]
        friends2 = json.loads(friends_json2)
        new_friend2 = {'id':self.player.low_id,'state':3}
        friends2.append(new_friend2)
        friends_json2 = json.dumps(friends2)
        cursor.execute('UPDATE plrs SET friends=? WHERE lowID=?', (friends_json2, self.LowID))
        conn.commit()
        conn.close()