import art4
print(art4.logo)


# TODO-2: Save data into dictionary {name: n
def find_highest_bidder(bidding_dictionary):
    winner =""
    highest_bid = 0



    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# TODO-3: Whether if new bids need to be added
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?:")
    price = int(input("What is your bid price?:$"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)