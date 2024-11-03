import os
from gavel_art import display_art
from auction_winner_logic import highest_bidder

auction_record = {}

while True:
    display_art()
    name = input("Enter Your/Organization's Name: ")
    if name.lower() in ['stop','/s','terminate','/t',' ']:
        break
    elif name in auction_record :
        print ("You Have Already Placed Your Bid!")
        continue
    else:
        bid = input("Bidding Amount: ")
        if bid.lower() in ['stop','/s','terminate','/t',' ']:
            break
        else:
            auction_record[name] = int(bid)

    os.system('cls' if os.name == 'nt' else 'clear')
print(" ")

if len(auction_record) > 0:
    highest_bidder(auction_record)
else:
    print("We Hope To See You Soon!")