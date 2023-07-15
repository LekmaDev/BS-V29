from Server.Login.LoginOkMessage import LoginOkMessage
from Server.Home.OwnHomeDataMessage import OwnHomeDataMessage 
from Server.Team.TeamMessage import TeamMessage
from Server.Login.LoginFailedMessage import LoginFailedMessage
from Utils.Reader import BSMessageReader
from Utils.Helpers import Helpers
from database.DataBase import DataBase
from Server.Club.AllianceStreamMessage import AllianceStreamMessage
from Server.Club.MyAllianceMessage import MyAllianceMessage
import os
import sqlite3 as sql
import random
from Server.Friend.FriendListMessage import FriendListMessage
class LoginMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.high_id = self.read_int()
        self.player.low_id = self.read_int()
        self.player.token = self.read_string()
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()
        self.fingerprint_sha = self.read_string()
        self.read_int()


    def process(self):
        if self.player.low_id != 0:
            LoginOkMessage(self.client, self.player).send()
            DataBase.loadAccount(self) # load account
            OwnHomeDataMessage(self.client, self.player).send()
            try:
                MyAllianceMessage(self.client, self.player, self.player.club_low_id).send()
                AllianceStreamMessage(self.client, self.player, self.player.club_low_id, 0).send()
                DataBase.GetmsgCount(self, self.player.club_low_id)
                FriendListMessage(self.client, self.player).send()
                DataBase.replaceValue(self, 'roomID', 0)
            except:
                MyAllianceMessage(self.client, self.player, 0).send()
                AllianceStreamMessage(self.client, self.player, 0, 0).send()
        elif self.player.low_id == 1:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Аккаунт не найден удалите все данные о игре!").send()
        elif self.player.low_id == 0:
            if os.path.exists("database/Player/plr.db"):
                self.conn = sql.connect("database/Player/plr.db")
                self.cur = self.conn.cursor()
                self.cur.execute("SELECT COUNT(*) FROM plrs")
                result = self.cur.fetchone()
                record_count = result[0] if result else 0
                self.player.low_id = record_count + 1
            else:
                self.player.low_id = 2
            self.player.high_id = 0
            self.player.token = Helpers.randomStringDigits(self)
            DataBase.createAccount(self)
            LoginOkMessage(self.client, self.player).send()
            OwnHomeDataMessage(self.client, self.player).send()
            MyAllianceMessage(self.client, self.player, self.player.club_low_id).send()
