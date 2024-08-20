bidding_finished = False
bids = {}


# bidding_record ={"Neelam": 100, "Ragini":200}
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of {highest_bid} value")



while not bidding_finished:
    name = input("What is your name?:")
    price = int(input("What is your bid price?:"))
    bids[name] = price
    should_continue = input("Are there any more bidders? Type Y or N:")
    if should_continue == "N":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue == 'Y':
        print()