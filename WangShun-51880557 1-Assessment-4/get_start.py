import random
from globalVariable import *
from BidderAgent import *
from Auctioneer import *

def start():
    commodity_Num = 3
    agents_Num = 3
    for i in range(1,commodity_Num+1):
        Commodity(i)
    for i in range(1,agents_Num+1):
        Agent(i)
    Auctioneer(0)
    for auctioneer in auctioneer_ID:
        auctioneer.Auction_Commodity()

start()