def highest_bidder(bidding_dictonary):
    winner = ""
    highest_bid = 0

    max(bidding_dictonary)

    for bidder in bidding_dictonary:
        bid_amount = bidding_dictonary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Types 'yes' or 'no'. \n")
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
    

