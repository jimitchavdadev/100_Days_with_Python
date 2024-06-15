logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
"""

import random

def sum(cards):
    sum=0
    for i in cards:
        sum+=i
    return sum

print(logo)

# List of card values in Blackjack (Ace can be 11 or 1, hence represented as 11 initially)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards=[]
computer_cards=[]

# Function to randomly append a card to the user's hand
def user_appends():
    tmp=random.choice(cards)
    user_cards.append(tmp)
    cards.remove(tmp)

# Function to randomly append a card to the computer's hand
def comp_appends():
    tmp=random.choice(cards)
    computer_cards.append(tmp)
    cards.remove(tmp)

# Initial card distribution
user_appends()
user_appends()
comp_appends()
comp_appends()
comp_choices=[True,False]  # Random choice for the computer to draw another card

# Game loop
while(True):
    print(user_cards)
    print(computer_cards[0])  # Show only one of the computer's cards

    choice=input("Type 'y' to get another card, type 'n' to pass: ")
    if choice=="y":
        user_appends()
        if random.choice(comp_choices)==True:  # Computer's random choice to draw another card
            comp_appends()
    else:
        if random.choice(comp_choices)==True:  # Computer's random choice to draw another card
            comp_appends()
            
    print("Your final hand: ", user_cards)
    print("Computer's final hand: ", computer_cards[0])  # Show only one of the computer's cards

    # Check win/lose conditions
    if sum(user_cards)>21 or sum(computer_cards)==21:
        print("You Lose! You went over 21!")
        print("Computer's final hand ", computer_cards)
        break
    elif sum(computer_cards)>21 or sum(user_cards)==21:
        print("You Win! The computer went over 21")
        print("Computer's final hand ", computer_cards)
        break

    # Compare sums to determine the winner
    if sum(user_cards)>sum(computer_cards):
        print("You win!")
        break
    elif sum(user_cards)<sum(computer_cards):
        print("You lose, computer's cards were: ", computer_cards)
        break