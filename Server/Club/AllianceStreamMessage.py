from database.DataBase import DataBase
import sqlite3 as sql
from Utils.Writer import Writer


class AllianceStreamMessage(Writer):

    def __init__(self, client, player, clubLowID, type):
        super().__init__(client)
        # self.msg_content = msg_content
        self.id = 24311
        self.player = player
        self.eventType = type
        self.clubLowID = clubLowID

    def encode(self):
        if self.clubLowID != 0:
            DataBase.GetmsgCount(self, self.clubLowID)
            self.writeVint(self.MessageCount) # Message count
            clubid = self.player.club_low_id
            self.conn = sql.connect("database/Club/clubs.db")
            self.con = sql.connect("database/Club/chats.db")
            self.cur= self.conn.cursor()
            self.chat = self.con.cursor()
            self.chat.execute(f"SELECT * FROM chats WHERE clubID={clubid}")
            fetch = self.chat.fetchall()
            for i in fetch:
                self.writeVint(i[1])
                self.writeVint(0)
                self.writeVint(i[2])
                self.writeVint(0)
                self.writeVint(i[3])
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
            self.writeVint(0)