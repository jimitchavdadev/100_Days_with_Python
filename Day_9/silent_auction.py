logo="""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
"""

print(logo)
print("Welcome to secret auction program! ")

def max_bid(bidders):
    max=0
    winner=""
    for i in bidders:
        if bidders[i]>max:
            max=bidders[i]
            winner=i
    print(f"The winner of the auction is {winner} with the bid of ${max}")

bidders={}

while(True):
    name=input("What is your name? ")
    bid=int(input("enter your bid: "))
    bidders[name]=bid
    choice=input("type 'new' to enter a bidder or any other key to exit: ")
    if choice=="new":
        continue
    else:
        max_bid(bidders)
        break

