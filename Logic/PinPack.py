from Utils.Writer import Writer
import random 
from database.DataBase import DataBase

class PinPack(Writer):

    def __init__(self, client, player, boxx=0):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.boxx = boxx

    def encode(self):
   	#logic resourse
		#end
        self.writeVint(203)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(100)#бокс ид 
        self.writeVint(1)#количество предметов
        self.writeVint(1) # Reward amount
        self.writeVint(0) # CsvID 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, self.boxx) # CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        self.writeVint(0)
        #DataBase.replaceValue(self, 'gold', self.player.gold + gold)
        self.writeBoolean(False)
        self.writeVint(0)
        self.writeLogicLong(-1)