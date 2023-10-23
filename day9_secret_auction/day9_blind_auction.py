from os import system
from art import logo


def show_winner(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        if highest_bid < bidding_record[bidder]:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")


bids = {}
keep_bidding = True

while keep_bidding:
    print(logo)
    name = input("Welcome to blind auction, what's is your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if another_bidder.lower() == "yes":
        system("cls")
    elif another_bidder.lower() == "no":
        keep_bidding = False
        system("cls")

print(logo)
show_winner(bidding_record=bids)
