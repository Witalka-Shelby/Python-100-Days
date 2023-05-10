from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

auction_dictionary = {}
auction_is_going = True

def get_bid_and_name():
    global auction_is_going
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dictionary[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "no":
        auction_is_going = False

def find_highest_bidder(bidding_record):
    for key in bidding_record:
        winner = key
        winning_bid = bidding_record[key]
        if bidding_record[key] > winning_bid:
            winner = key
            winning_bid = bidding_record[key]

    print(f"The winner is {winner} with a bid of ${winning_bid}.")

while auction_is_going:
    get_bid_and_name()
    os.system("cls")

find_highest_bidder(auction_dictionary)