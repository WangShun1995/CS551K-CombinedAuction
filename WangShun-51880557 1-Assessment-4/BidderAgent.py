import random
from globalVariable import *

class Agent():
    def __init__(self,ID):
        self.ID = ID
        self.money = random.randint(30,100)
        self.massage = set()
        self.commodity = set()
        bidderAgent_ID.add(self)

    def send(self,type,commodity,price):
        for auctioneer in auctioneer_ID:
            auctioneer.massage.add(Massage(self,type,commodity,price))
            #print(self.ID, price)


    def receive_massage(self):
        #print("zzzzzzzzz")
        for massage in self.massage:
            if massage.type == 0:
                '''print(self.ID," prepared to auction.")'''
            elif massage.type == 1:
                self.bid(massage.commodity,massage.price)
                #print(self.ID, " receive price.")
            elif massage.type == 2:
                '''print(self.ID, " price be accepted.")'''
            elif massage.type == 3:
                '''print(self.ID, " price be refused.")'''
            elif massage.type == 4:
                self.money = self.money - massage.price
                self.commodity.add(massage.commodity)
                #print("Bidder ",self.ID,": wins the auction of commodity",massage.commodity.ID,'!')
            else:
                print("Bidder ",self.ID,": Error!")
        self.massage.clear()

    def bid(self,commodityID,price):
        for auctioneer in auctioneer_ID:
            if auctioneer.auction == 1:
                rate = random.random()* 0.3
                if price <= self.money:
                    if int(price*rate) <= self.money:
                        self.send(11,commodityID,int(price*(1+rate)))
                    else:
                        self.send(11,commodityID,self.money)
            elif auctioneer.auction == 0:
                if price < self.money:
                    self.send(12,commodityID,price)