# Define the logo for the secret auction program
logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
"""

# Print the logo and welcome message
print(logo)
print("Welcome to the secret auction program!")

# Function to find the maximum bid and winner
def max_bid(bidders):
    max_bid = 0  # Initialize the maximum bid to zero
    winner = ""  # Initialize the winner's name as an empty string
    for bidder in bidders:
        if bidders[bidder] > max_bid:  # Check if the bidder's bid is greater than the current maximum bid
            max_bid = bidders[bidder]  # Update the maximum bid
            winner = bidder  # Update the winner's name
    print(f"The winner of the auction is {winner} with a bid of ${max_bid}")  # Print the winner and their bid

bidders = {}  # Initialize an empty dictionary to store bidders and their bids

# Loop to collect bidders and their bids
while True:
    name = input("What is your name? ")  # Get bidder's name
    bid = int(input("Enter your bid: "))  # Get bidder's bid
    bidders[name] = bid  # Add bidder and their bid to the dictionary
    choice = input("Type 'new' to enter a new bidder or any other key to exit: ")  # Ask if user wants to add more bidders
    if choice.lower() == "new":  # Check if user wants to add more bidders
        continue  # Continue to the next iteration of the loop
    else:
        max_bid(bidders)  # Call the function to find the winner and maximum bid
        break  # Exit the loop