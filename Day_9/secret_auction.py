# Secret Auction

from replit import clear
print("welcome to the secret auction program")

def add_bidder(name, bid):
    new_entry={
        "name":name,
        "bid":bid
        }
    auction_data.append(new_entry)

auction_data=[]

def find_highest_bidder(data):
    max=0
    winner=""
    for bidder in auction_data:
        if bidder["bid"] > max:
            max=bidder["bid"]
            winner=bidder["name"]
    print(f"the winner of the auction is {winner} with the bid of ${max}")
    
while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bidder(name, bid)
    choice = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if choice == "no":
        break
    clear()

find_highest_bidder(auction_data)