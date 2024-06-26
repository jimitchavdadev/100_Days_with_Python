# Treasure Island Game

# Print the ASCII art for the game's starting screen
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Function to handle the door choice after waiting
def wait():
    # Prompt the user to choose a door and convert the input to lowercase
    choice = input("Which door? ").lower()
    if choice == "red":
        print("Burned by fire. Game over.")
    elif choice == "yellow":
        print("You Win!")
    elif choice == "blue":
        print("Eaten by beasts. Game over.")
    else:
        print("Game over.")

# Function to handle the choice at the river
def left():
    # Prompt the user to choose between swimming or waiting
    choice = input("Swim or wait? ").lower()
    if choice == "swim":
        print("Attacked by a trout. Game over.")
    elif choice == "wait":
        wait()

# Print the welcome message and the mission objective
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Prompt the user to choose a direction at the cross road
choice = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice == "left":
    left()
else:
    print("Fall into a hole. Game over.")