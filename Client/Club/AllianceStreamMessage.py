from Server.Club.AllianceChatServer import AllianceChatServer
from Server.Club.AllianceBotChatServerMessage import AllianceBotChatServerMessage
from database.DataBase import DataBase
from Utils.Reader import BSMessageReader
from Server.Login.LoginFailedMessage import LoginFailedMessage


class AllianceStreamMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string()
        if self.msg.lower() == '/theme':
            if self.player.vip == 1:
                self.bot_msg = f'Выбери айди темы\n0 - Обычная\n1 - Новый год (Снег)\n2 - Красный новый год\n3 - От клеш рояля\n5 - Желтые панды\n6 - Фиолетовый булл\n7 - Роботы Зелёный фон\n8 - Фиолетовый фон\n9 - Пиратский фон\n11 - Футбольный фон\nИспользовать команду /theme ID'
                self.IsAcmd = True
            else:
                self.bot_msg = f'У тебя нет привилегии VIP\nПиши в тг @itdlaloxov что бы купить'
                self.IsAcmd = True
        if self.msg.lower().startswith('/theme'):
            if self.player.vip == 1:
                try:
                    newStarpoints = self.msg.split(" ", 6)[1:]
                    DataBase.replaceValue(self, 'theme', int(newStarpoints[0]))
                    self.bot_msg = f'перезайти в игру фон был успешно изменен'
                    self.IsAcmd = True
                except:
                    pass
            else:
                self.bot_msg = f'У тебя нет привилегии VIP\nПиши в тг @itdlaloxov что бы купить'
                self.IsAcmd = True

    def process(self):
        if self.send_ofs == False and self.IsAcmd == False:
            DataBase.Addmsg(self, self.player.club_low_id, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServer(self.client, self.player, self.msg, self.player.club_low_id).send()
        if self.bot_msg != '':
            AllianceChatServer(self.client, self.player, self.msg, self.player.club_low_id, True).send()
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()