from Utils.Writer import Writer
from database.DataBase import DataBase
import sqlite3 as sql
class AllianceChatServer(Writer):

    def __init__(self, client, player, msg_content, clubID, isbot=False):
        super().__init__(client)
        self.msg_content = msg_content
        self.id = 24312
        self.player = player
        self.clubID = clubID
        self.isbot = isbot
        self.client = client

    def encode(self):
        DataBase.GetmsgCount(self, self.clubID)
        clubid = self.player.club_low_id
        self.conn = sql.connect("database/Club/clubs.db")
        self.con = sql.connect("database/Club/chats.db")
        self.cur= self.conn.cursor()
        self.chat = self.con.cursor()
        
        self.chat.execute(f"SELECT * FROM chats WHERE clubID={clubid}")
        fetch = self.chat.fetchall()
        	#AllianceStreamMessage(self.client, self.player, self.player.club_low_id, 0).send()
        i = fetch[len(fetch)-1]
        if self.isbot == False:
            self.writeVint(i[1])
            self.writeVint(0)
            self.writeVint(len(fetch))
            self.writeVint(0)
            self.writeVint(i[3])#plrid
            self.writeString(i[4])
            self.writeVint(i[5])
            self.writeVint(0)
            self.writeVint(0)
            if i[1] == 4:
               self.writeVint(int(i[6]))#1 = Kicked, 2 = Join request accepted, 3 = Join the club, 4 = Leave the club
               self.writeVint(1)
               self.writeVint(0)
               self.writeVint(i[3])
               self.writeString(i[4])
            else:
               self.writeString(i[6])
        else:
            self.writeVint(i[1])
            self.writeVint(0)
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(i[3])#plrid
            self.writeString(i[4])
            self.writeVint(i[5])
            self.writeVint(0)
            self.writeVint(0)
            self.writeString(i[6])