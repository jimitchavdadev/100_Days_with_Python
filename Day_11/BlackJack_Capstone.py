logo="""
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

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards=[]
computer_cards=[]

def user_appends():
    tmp=random.choice(cards)
    user_cards.append(tmp)
    cards.remove(tmp)

def comp_appends():
    tmp=random.choice(cards)
    computer_cards.append(tmp)
    cards.remove(tmp)


user_appends()
user_appends()
comp_appends()
comp_appends()
comp_choices=[True,False]

while(True):
    print(user_cards)
    print(computer_cards[0])

    choice=input("Type 'y' to get another card, type 'n' to pass: ")
    if choice=="y":
        user_appends()
        if random.choice(comp_choices)==True:
            comp_appends()
    else:
        if random.choice(comp_choices)==True:
            comp_appends()
            
    print("your final hand: ",user_cards)
    print("computer's final hand: ",computer_cards[0])

    if sum(user_cards)>21 or sum(computer_cards)==21:
        print("You Lose! You went over 21!")
        print("computer's final hand ", computer_cards)
        break
    elif sum(computer_cards)>21 or sum(user_cards)==21:
        print("You Win! The computer went over 21")
        print("computer's final hand ", computer_cards)
        break

    if sum(user_cards)>sum(computer_cards):
        print("you win!")
        break
    elif sum(user_cards)<sum(computer_cards):
        print("you lose, computer's cards were: ",computer_cards)
        break