from Utils.Writer import Writer
from Logic.Commands.Server.LogicSetSupportedCreatorCommand import LogicSetSupportedCreatorCommand

class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.commandID = commandID

    def encode(self):

        commands = {
            215: LogicSetSupportedCreatorCommand
        }

        if self.commandID in commands:
            self.writeVint(self.commandID)
            commands[self.commandID].encode(self)