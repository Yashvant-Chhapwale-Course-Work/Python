
def highest_bidder(bidding_dictionary):
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