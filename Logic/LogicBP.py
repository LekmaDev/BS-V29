from Utils.Writer import Writer
class LogicBP(Writer):
    def __init__(self, client, player,bp, ids, c, i, b, s, p):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.bp = bp
        self.ids = ids
        self.c = c
        self.i = i
        self.b = b
        self.p = p
        self.s = s

    def encode(self):
        self.writeVint(203) # Command
        
        self.writeVint(0)
        self.writeVint(1) # Multipler
        self.writeVint(100) # type (box id)
        self.writeVint(1) # Reward Count
        if self.i == 1:
            self.writeVint(1)# Reward amount
            self.writeScId(16, self.b)  # CsvID 16
            self.writeVint(1) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
        elif self.i == 6:
            self.writeVint(self.c) # Reward amount
            self.writeScId(16, self.b) # CsvID 16
            self.writeVint(6) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) 
        elif self.i == 8 or self.i == 7:#gold // gems
            self.writeVint(self.c) # Reward amount
            self.writeVint(0) # CsvID 16
            self.writeVint(self.i) # Reward ID
            self.writeVint(0) # CsvID 29
            self.writeVint(0) # CsvID 52
            self.writeVint(0) # CsvID 23
            self.writeVint(0) # ????
        elif self.i == 9:#skin
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(9)
            self.writeScId(29, self.s[1])# 29
            self.writeVint(0)# 52
            self.writeVint(0)# 23
            self.writeVint(0)

        self.writeBoolean(False)

        self.writeVint(self.bp)#RewardTrackType
        self.writeVint(self.ids+2)#RewardForRank
        self.writeVint(0)

        self.writeVint(1)