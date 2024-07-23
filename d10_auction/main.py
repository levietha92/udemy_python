
#This is my own answer
import art
from replit import clear

# defining function
bidders = []
def take_bidder_info():
  clear()
  bidder = {}
  name = input("What is your name?")
  bid = input("What is your bid?")
  bidder["name"] = name
  bidder["bid_amount"] = int(bid)
  
  bidders.append(bidder)
  return bidders

#run the bid
print(art.logo)
multiple = "yes"
name_list = []
bid_amt_list = []

while multiple == "yes":
  take_bidder_info()
  multiple = input("Are there anyone else? yes/no ")

if multiple == "no":
  print(bidders)
  #start comparing the bidders
  for x in bidders:
    bid_amt_list.append(x["bid_amount"])
    name_list.append(x["name"])

# print(bid_amt_list)
# print(max(bid_amt_list))
winner_bid_amount = max(bid_amt_list)
winner_index = bid_amt_list.index(winner_bid_amount)

winner = name_list[winner_index]

print(f"The winner of the auction is {winner} at ${winner_bid_amount}")