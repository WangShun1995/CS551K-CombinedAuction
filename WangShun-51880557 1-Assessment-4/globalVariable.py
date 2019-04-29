import random
auctioneer_ID = set()
bidderAgent_ID = set()

commodityScale = set()

transTime = 3
totalTime = transTime*3


class Massage():
    def __init__(self,sender,type,commodity,price):
        self.sender = sender
        self.type = type
        self.commodity = commodity
        self.price = price

class Commodity():
    def __init__(self,ID):
        self.ID = ID
        self.initialPrice = random.randint(0,50)
        self.currentPrice = self.initialPrice
        self.transactionPrice = 0
        self.state = 'Auctioning'
        commodityScale.add(self)