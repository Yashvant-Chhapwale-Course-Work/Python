import os
from gavel_art import display_art
import auction_winner_logic

auction_record = {}

while True:
    display_art()
    name = input("Enter Your/Organization's Name: ")
    if name.lower() in ['stop','/s','terminate','/t']:
        break
    elif name in auction_record :
        os.system('cls' if os.name == 'nt' else 'clear') #Prevents the same bidder from updating bids!
        print ("You Have Already Placed Your Bid!")
        continue
    else:
        bid = input("Bidding Amount: ")
        if bid.lower() in ['stop','/s','terminate','/t']:
            break
        elif any(input in [""," "] for input in [name,bid]): #Prohibits Empty Submissions ("", " ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("A field cannot be left blank!")
            continue
        else:
            auction_record[name] = int(bid)

    os.system('cls' if os.name == 'nt' else 'clear') #This code removes the previous output in the shell, before prompting for the next bid input.
print(" ")

#The 'if-else' part ahead is unnecessary for 'highest_bidderv1()' ,it can be directly executed as it handles empty 'bit_dictionary' case internally.But, it is necessary for 'highest_bidderv0()'.
if len(auction_record) > 0: 
    auction_winner_logic.highest_bidderv1(auction_record)
else:
    print("We Hope To See You Soon!")