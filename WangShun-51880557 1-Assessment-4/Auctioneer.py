from globalVariable import *

class Auctioneer():
    def __init__(self,ID):
        self.ID = ID
        self.massage = set()
        self.commodity = set()
        self.auction = 1
        auctioneer_ID.add(self)

    def send(self,receivers,type,commodity,price):
        receivers.massage.add(Massage(self,type,commodity,price))

    def EnglishAuction(self,commodity):
        acceptPrice = commodity.currentPrice
        turnWinnerID = 0
        for massage in self.massage:
            if massage.commodity != commodity:
                continue
            if massage.type == 11:
                if massage.price > acceptPrice:
                    if turnWinnerID != 0:
                        self.send(turnWinnerID,3,commodity,massage.price)
                    acceptPrice = massage.price
                    turnWinnerID = massage.sender
                else:
                    self.send(massage.sender,3,commodity,acceptPrice)
        if turnWinnerID != 0 and acceptPrice >= int(commodity.currentPrice*1.05):
            for agent in bidderAgent_ID:
                self.send(agent,2,commodity,acceptPrice)
            commodity.currentPrice = acceptPrice
        elif turnWinnerID != 0:
            for agent in bidderAgent_ID:
                self.send(agent, 2, commodity, int(commodity.currentPrice*1.05))
            commodity.currentPrice = int(commodity.currentPrice*1.1)
        elif turnWinnerID == 0:
            return False
        return True


    def DutchAuction(self,commodity):
        for massage in self.massage:
            if massage.type == 12:
                print('No.',commodity.ID,"commodity has been sold to ", massage.sender.ID,". The price is ",commodity.currentPrice)
                self.send(massage.sender,4,commodity,commodity.currentPrice)
                return True
        return False

    def Auction_Commodity(self):
        for commodity in commodityScale:
            for agent in bidderAgent_ID:
                self.send(agent, 0, commodity, commodity.initialPrice)
            self.auction = 1
            transTime = 3
            #print("xxxxxxxxxxx")
            for t in range(totalTime,transTime,-1):
                for agent in bidderAgent_ID:
                    self.send(agent, 1, commodity, commodity.currentPrice)
                #print(commodity.currentPrice)
                for agent in bidderAgent_ID:
                    agent.receive_massage()
                if self.EnglishAuction(commodity) == False:
                    transTime = t - 1
                    self.massage.clear()
                    break
                self.massage.clear()
            self.auction = 0
            for t in range(transTime,0,-1):
                for agent in bidderAgent_ID:
                    self.send(agent, 1, commodity, int(commodity.currentPrice*0.9))
                for agent in bidderAgent_ID:
                    agent.receive_massage()
                if self.DutchAuction(commodity) == True:
                    break
                else:
                    self.massage.clear()
                if t == 1:
                    print('No.',commodity.ID,"commodity fail to sell.")