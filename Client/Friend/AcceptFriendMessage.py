from Utils.Reader import BSMessageReader
import sqlite3
import json
from Server.Friend.FriendListMessage import FriendListMessage

class AcceptFriendMessage(BSMessageReader):

    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.a = self.read_int()
        self.b = self.read_int()

    def process(self):
        conn = sqlite3.connect('database/Player/plr.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.player.low_id,))
        user = cursor.fetchone()
        friends_json = user[22]
        friends = json.loads(friends_json)
        for item in friends:
        	if item['id'] == self.b:
        		item['state'] = 4
        		friends_json = json.dumps(friends)
        		break
        friends_json = json.dumps(friends)
        cursor.execute('UPDATE plrs SET friends=? WHERE lowID=?', (friends_json, self.player.low_id))
        conn.commit()
        conn.close()
        
        
        
        conn = sqlite3.connect('database/Player/plr.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plrs WHERE lowID=?', (self.b,))
        user = cursor.fetchone()
        friends_json = user[22]
        friends = json.loads(friends_json)
        for item in friends:
        	if item['id'] == self.player.low_id:
        		item['state'] = 4
        		friends_json = json.dumps(friends)
        		break
        friends_json = json.dumps(friends)
        cursor.execute('UPDATE plrs SET friends=? WHERE lowID=?', (friends_json, self.b))
        conn.commit()
        conn.close()
        FriendListMessage(self.client, self.player).send()