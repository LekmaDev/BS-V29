from Utils.Writer import Writer
from database.DataBase import DataBase
from Logic.Shop import Shop
from Logic.Quest import Quest
from Utils.Helpers import Helpers
import json
from datetime import datetime
from Server.Club.AllianceDataMessage import AllianceDataMessage
import time
from Logic.EventSlots import EventSlots
from Server.Login.LoginFailedMessage import LoginFailedMessage

class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player
        self.timestamp = int(datetime.timestamp(datetime.now()))

    def encode(self):
        config = open('config.json', 'r')
        content = config.read()
        settings = json.loads(content)
        first = time.time()
        DataBase.loadAccount(self)
        sec = time.time()
        final = sec-first
        #NotifManager(self.player, self.client).SeasonEnd()
        self.writeVint(9999) # Timestamp
        self.writeVint(124670) # Timestamp

        self.writeVint(self.player.trophies)  # Player Trophies
        self.writeVint(self.player.highest_trophies)  # Player Max Reached Trophies
        self.writeVint(self.player.highest_trophies)
        self.writeVint(self.player.Troproad)  # Trophy Road Reward

        self.writeVint(220 + self.player.player_experience)  # Player Experience

        self.writeScId(28, self.player.profile_icon) # Player Profile Icon
        self.writeScId(43, self.player.name_color) # Player Name Color

        self.writeVint(0) # Count

        # Selected Skins Array
        self.writeVint(1)
        self.writeScId(29,self.player.skin_id)
        # Selected Skins Array End

        # Unlocked Skins Array
        self.writeVint(len(self.player.UnlockedSkins))
        for i in self.player.UnlockedSkins:
            if self.player.UnlockedSkins[str(i)]==1:
                self.writeScId(29, int(i))
            else:
                self.writeScId(29, 0)
        # Unlocked Skins Array End
       
        # Unknown Skins Array
        self.writeVint(0)
        # Unknown Skins Array End
        
        self.writeVint(0)
        self.writeVint(self.player.highest_trophies)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)
        
        self.writeVint(0) # Remaining Tokens Doubler
        self.writeVint(3600000)  # Trophy League Season Timer
        self.writeVint(0)
        self.writeVint(3600000) # Brawl Pass Season Timer
        
        self.writeVint(0)
        self.writeBoolean(True)
        
        # Unknown Array
        self.writeBoolean(True)
        self.writeVint(0)
        # Unknown Array End

        self.writeByte(4)  # Shop Token Doubler Related
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        
        self.writeVint(0) # Change Name Cost in Gems
        self.writeVint(0) # Timer For The Next Name Change
        
        # Shop Array
        Shop.EncodeShopOffers(self)
        # Shop Array End
        
        # Brawl Box Ads Array
        self.writeVint(1)
        for x in range (1):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(10)
        # Brawl Box Ads Array End
            
        self.writeVint(200) # Battle tokens
        self.writeVint(0)  # Time till Bonus Tokens (seconds)
        
        # Unknown Array
        self.writeVint(0) # Count
        # Unknown Array End
        
        self.writeVint(self.player.tickets)  # Tickets
        self.writeVint(0)
        
        self.writeScId(16, self.player.brawler_id) # Selected Brawler

        self.writeString("BY")  # Location
        self.writeString(f"{self.player.ccc}")  # Supported Content Creator
        
        # Unknown Array
        self.writeVint(1)# Count
        for x in range(1):
            self.writeInt(4)
        if self.player.bet >= 1:
            self.writeInt(self.player.bet)
        else:
            self.writeInt(0)
        if self.player.bet >= 1:
            self.player.bet = 0
        # Unknown Array End
            
        # Unknown Array
        self.writeVint(0)

        # Brawl Pass Array
        self.writeBoolean(True)  # Brawl Pass Boolean

        self.writeVint(0)  # 0-Гейл 1- Волт 2- Коллет
        self.writeVint(self.player.BPTOKEN)  # Brawl Pass Collected Tokens
        if self.player.low_id in settings['buybp']:
            self.writeVint(1)
        else:
            self.writeVint(0)
        self.writeVint(0)  # Collected Tier

        self.writeByte(1)  # Unknown array
        self.writeInt(self.player.buypass) 
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeByte(1)  # Unknown array
        self.writeInt(self.player.freepass)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        # Brawl Pass Array End

        self.writeVint(1) #silovaya liga?
        for x in range(1):
            self.writeVint(0)
            self.writeVint(0)

        # Quests Array
        Quest.EncodeQuest(self)
        # Quests Array End
        
        # Emotes Array
        self.writeBoolean(True) # Emojis Boolean
        self.writeVint(0)
        
        # Region Home
        self.writeVint(2019049) # Shop Timestamp
        self.writeVint(100) # Brawl Box Tokens
        self.writeVint(10) # Big Box Tokens

        for item in Shop.boxes:
            self.writeVint(item['Cost'])
            self.writeVint(item['Multiplier'])

        self.writeVint(Shop.token_doubler['Cost'])
        self.writeVint(Shop.token_doubler['Amount'])

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)
        
        #Unkown array
        self.writeVint(0)
        
        # Logic Events Count Array
        count = len(EventSlots.maps)
        self.writeVint(count + 1)  # Event slot count
        for i in range(count + 1):
            self.writeVint(i)
        # Logic Events Count Array End
        
        # Logic Events Array
        self.writeVint(count)
        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(3600)  # Timer

            self.writeVint(map['Tokens'])
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString('') # "Double Experience Event" Text
            self.writeVint(2) # State?
            self.writeVint(0)  # Powerplay game played
            self.writeVint(1) # Powerplay game left maximum
            self.writeVint(1) #Modifiers count
            self.writeVint(map['Modifier']) #Modifier
            self.writeVint(0) #Championship Wins
            self.writeVint(0) #Championship Type (0 = Championship, 1 = PSG Cup)
        # Logic Events Array End
            
        # Upcoming Events Array
        self.writeVint(1)
        
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)  # IsActive | 0 = Active, 1 = Disabled
        self.writeVint(3600)  # Timer

        self.writeVint(0)
        self.writeScId(15, 32)

        self.writeVint(2)

        self.writeString() # "Double Experience Event" Text
        self.writeVint(0)
        self.writeVint(0)  # Powerplay game played
        self.writeVint(3)  # Powerplay game left maximum
        self.writeVint(0) # Modifier array
        self.writeVint(0)
        self.writeVint(1)
        # Upcoming Events Array End
        
            
        # Logic Shop
        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:  # Tickets Price
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:  # Tickets Amount
            self.writeVint(i)

        self.writeVint(1)#GOLD PACK #1
        self.writeVint(10)#GOLD PACK cOST #1

        self.writeVint(1)#GOLD PACK #1
        self.writeVint(1337)#GOLD PACK aMMO #1

        self.writeVint(0) 
        self.writeVint(200) # Maximun Battle Tokens
        self.writeVint(20) # Tokens Gained in Refresh
        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeBoolean(True)  # Box boolean
        
        # Unknown Array
        self.writeVint(0)
        # Unknown Array End
        
        # Menu Themes Array
        self.writeVint(1)  # Count
        self.writeInt(1)
        self.writeInt(41000000 + self.player.theme)
        # Menu Themes Array End
        
        # Unknown Array
        self.writeVint(0)
        # Unknown Array End
        
        # Unknown Array
        self.writeVint(0)
        # Unknown Array End

        self.writeInt(self.player.high_id)  # High Id
        self.writeInt(self.player.low_id)  # Low Id
        self.writeVint(1)  # array
        # Custom Support Message Notification
        self.writeVint(81) # Notification ID
        self.writeInt(1) # Notification Index
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString(f"Добро пожаловать в <c8bfd28>V<c68fb51>B<c45f97a>C<c22f7a3> <c09f5cc>B<c00f5cc>R<c19f7a3>A<c33f97a>W<c4cfb51>L</c>!\nТвой ID: <c57fa66>{self.player.low_id}</c>\nКупить привилегию VIP TG - <c05f971>@<c0af481>i<c0fef91>t<c14eaa0>d<c19e5b0>l<c1edfbf>a<c1fe0c0>l<c19e5a0>o<c14ea80>x<c0fef60>o<c0af440>v</c>\nНовостной <c82fc33>T<c57fa66>e<c2bf799>l<c00f5cc>e<c20f799>g<c40fa66>r<c60fc33>a<c80ff00>m</c> канал: t.me/vbcbrawl\n") # Notification Message Entry       
        self.writeVint(0)
        self.writeVint(0)
        self.writeBoolean(True)

        self.writeBoolean(False)
        
        self.writeVint(0)

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        if self.player.name == "VBC26":
            self.writeString("VBC26")  # Player Name
            self.writeVint(0)
        else:
            self.writeString(f"{self.player.name}")  # Player Name
            self.writeVint(1)
        self.writeInt(0)
        
        self.writeVint(8) # Commodity Count
        self.writeVint(len(self.player.card_unlock_id) + 4)  # count

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeScId(23, unlock_id)
            try:
                self.writeVint(self.player.UnlockedBrawlers[str(index)])
            except:
                self.writeVint(1)
            index += 1
                        
        self.writeScId(5, 1)  # Resource ID
        self.writeVint(0)# brawlbox

        self.writeScId(5, 8)  # Resource ID
        self.writeVint(self.player.gold) # Coins Amount

        self.writeScId(5, 9)  # Resource ID
        self.writeVint(0) # Star Tokens Amount
        
        self.writeScId(5, 10)  # Resource ID
        self.writeVint(self.player.starpoints) # Star Points Array

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlers_trophies))  # brawlers count
        for brawler_id, trophies in self.player.brawlers_trophies.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlers_trophies[f"{int(brawler_id)}"])


        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlers_trophies))  # brawlers count
        for brawler_id, trophies in self.player.brawlers_trophies.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlers_trophies[f"{int(brawler_id)}"])

        self.writeVint(0)  # array

        # Brawlers Upgrade Points array
        self.writeVint(len(self.player.brawlerPoints))  # brawlers count
        for brawler_id, trophies in self.player.brawlerPoints.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlerPoints[f"{int(brawler_id)}"])

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlerPowerLevel))  # brawlers count
        for brawler_id, trophies in self.player.brawlerPowerLevel.items():
                self.writeScId(16, int(brawler_id))
                self.writeVint(self.player.brawlerPowerLevel[f"{int(brawler_id)}"])
        # Brawlers Power Level Array End

    # Gadgets and Star Powers array
        self.writeVint(1)  # count
        self.writeVint(23)
        self.writeVint(3)
        self.writeVint(1)
        self.writeVint(0)
        
        self.writeVint(self.player.gems)  # Player Gems
        self.writeVint(0)  # Player Gems
        self.writeVint(0) # Tips Related
        self.writeVint(0) # Unknown
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2) # Tutorial State
        self.writeVint(1585502369)
        if self.player.low_id == 1:
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Аккаунт не найден удалите все данные о игре!").send()
        elif self.player.low_id > 1:
            DataBase.replaceValue(self, "online", 2)
            if self.player.gold < 0:
                self.player.gold = 0
                DataBase.replaceValue(self, 'gold', self.player.gold)
            if self.player.gems < 0:
                self.player.gems = 0
                DataBase.replaceValue(self, 'gems', self.player.gems)
            if self.player.low_id in settings['vips']:
                DataBase.replaceValue(self, 'vip', 1)
            if self.player.low_id in settings['banID']:
                update_url = 'https://t.me/vbcsupport_bot'
                self.player.err_code = 11
                LoginFailedMessage(self.client, self.player, "Вы были заблокированы! Подать на аппеляцию можно написав боту - @vbcsupport_bot").send()