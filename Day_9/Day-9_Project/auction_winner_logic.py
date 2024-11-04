def highest_bidderv0(bidding_dictionary):
    winner = ""
    highest_bid = 0
    tie = []

    for bidder in bidding_dictionary:
        bid = bidding_dictionary[bidder]
        if highest_bid < bid:
            highest_bid = bid
            winner = bidder
            tie=[]  # Starts a New Tie_List with the Current Highest Bidder
            tie.append(bidder)
        elif highest_bid == bid:
            tie.append(bidder)
    
    if len(tie)>1:
        print(f"We have a tie! The following Bidders have placed an equal Highest Bid of ₹{highest_bid}: ")
        for bidder in tie:
            print(f"Bidder: {bidder}")
    else:
        print(f'We are pleased to announce that the Highest Bid is ₹{highest_bid}, submitted by {winner}.')



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def highest_bidderv1(bidding_dictionary):
    if not bidding_dictionary:  # Check If The Dictionary Is Empty
        print("We Hope To See You Soon!")
        return

    highest_bid = max(bidding_dictionary.values()) #Using 'max()' to find the highest_bid value.
    
    winners = [bidder for bidder, bid in bidding_dictionary.items() if bid == highest_bid] #Finding all Bidders who placed the same 'highest_bid' amount(Examining for a Tie).
    
    if len(winners) > 1:
        print(f"We have a tie! The following bidders have placed an equal highest bid of ₹{highest_bid}:")
        for bidder in winners:
            print(f"Bidder: {bidder}")
    else:
        print(f'We are pleased to announce that the highest bid is ₹{highest_bid}, submitted by {winners[0]}.')


