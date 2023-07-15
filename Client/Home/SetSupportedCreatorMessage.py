from Utils.Reader import BSMessageReader
from database.DataBase import DataBase
from Server.Home.SetSupportedCreatorReponse import SetSupportedCreatorReponse
from Logic.Commands.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
import json

class SetSupportedCreatorMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.ccc = self.read_string()

    def process(self):
        config = open('config.json', 'r')
        content = config.read()
        settings = json.loads(content)
        if self.player.ccc == '':
            DataBase.replaceValue(self, 'SCC', self.player.ccc)
            AvailableServerCommandMessage(self.client, self.player, 215).send()
        elif self.player.ccc in settings['CCC']:
            DataBase.replaceValue(self, 'SCC', self.player.ccc)
            AvailableServerCommandMessage(self.client, self.player, 215).send()
        else:
            SetSupportedCreatorReponse(self.client, self.player).send()