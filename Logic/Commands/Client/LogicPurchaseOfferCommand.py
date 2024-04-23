from Logic.Commands.Client.LogicBoxDataCommand import LogicBoxDataCommand
from Utils.Reader import BSMessageReader
from Logic.Shop import Shop
from Logic.LogicBuy import LogicBuy
from database.DataBase import DataBase

class LogicPurchaseOfferCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.offer_index = self.read_Vint()


    def process(self):
        Shop.loadOffers(self)
        offers = self.offers
        id1 = offers[self.offer_index]['ID'][0]
        id2 = offers[self.offer_index]['ID'][1]
        id3 = offers[self.offer_index]['ID'][2]
        multi1 = offers[self.offer_index]['Multiplier'][0]
        multi2 = offers[self.offer_index]['Multiplier'][1]
        multi3 = offers[self.offer_index]['Multiplier'][2]
        brawler1 = offers[self.offer_index]['BrawlerID'][0]
        brawler2 = offers[self.offer_index]['BrawlerID'][1]
        brawler3 = offers[self.offer_index]['BrawlerID'][2]
        skin1 = offers[self.offer_index]['SkinID'][0]
        skin2 = offers[self.offer_index]['SkinID'][1]
        skin3 = offers[self.offer_index]['SkinID'][2]
        if offers[self.offer_index]['ShopType'] == 0:
            self.player.gems -= offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gems', self.player.gems)
        elif offers[self.offer_index]['ShopType'] == 1:
            self.player.gold -= offers[self.offer_index]['Cost']
            DataBase.replaceValue(self, 'gold', self.player.gold)
        else:
            pass#Нечего не найдено


        ID1 = 0
        ID2 = 0
        ID3 = 0


        if id1 == 1:
            ID1 = 1
        if id2 == 1:
            ID2 = 1
        if id3 == 1:
            ID3 = 1
        if id1 == 24:
            ID1 = 7
        if id2 == 24:
            ID2 = 7
        if id3 == 24:
            ID3 = 7            
        if id1 == 16:
            ID1 = 2
        if id2 == 16:
            ID2 = 2
        if id3 == 16:
            ID3 = 2
        if id1 == 5:
            ID1 = 3
        if id2 == 5:
            ID2 = 3
        if id3 == 5:
            ID3 = 3
        if id1 == 19:
            ID1 = 8 
        if id2 == 19:
            ID2 = 8 
        if id3 == 19:
            ID3 = 8 
        if id1 == 9:
            ID1 = 4
        if id2 == 9:
            ID2 = 4
        if id3 == 9:
            ID3 = 4
        if id1 == 8:
            ID1 = 5
        if id2 == 8:
            ID2 = 5
        if id3 == 8:
            ID3 = 5
        if id1 == 3:
            ID1 = 6
        if id2 == 3:
            ID2 = 6
        if id3 == 3:
            ID3 = 6

        if id1 == 4:
            ID1 = 7
        if id2 == 4:
            ID2 = 7
        if id3 == 4:
            ID3 = 7

        if id1 in [6, 10, 14]:
            if id1 == 6:
                LogicBoxDataCommand(self.client, self.player, 10).send()
                Shop.UpdateOfferData(self, self.offer_index)
            elif id1 == 10:
                LogicBoxDataCommand(self.client, self.player, 11).send()
                Shop.UpdateOfferData(self, self.offer_index)
            elif id1 == 14:
                LogicBoxDataCommand(self.client, self.player, 9).send()
                Shop.UpdateOfferData(self, self.offer_index)
        else:
            
            if id1 != 0 and id2 != 0 and id3 != 0:
                LogicBuy(self.client, self.player, ID1, ID2, ID3, multi1, multi2, multi3, brawler1, brawler2, brawler3, skin1, skin2, skin3).send()
                Shop.UpdateOfferData(self, self.offer_index)
            elif id1 != 0 and id2 != 0:
                LogicBuy(self.client, self.player, ID1, ID2, 0, multi1, multi2, 0, brawler1, brawler2, 0, skin1, skin2, 0).send()
                Shop.UpdateOfferData(self, self.offer_index)
            else:
                LogicBuy(self.client, self.player, ID1, 0, 0, multi1, 0, 0, brawler1, 0, 0, skin1, 0, 0).send()
                Shop.UpdateOfferData(self, self.offer_index)
