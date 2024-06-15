import random

# Dictionary to store the ASCII art for each option (Rock, Paper, Scissors)
option_logo = {
    0: """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    1: """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    2: """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# List to store the names of the options
option = ["Rock", "Paper", "Scissors"]

# Function to get the computer's choice randomly from the options list
def computer_choice():
    return random.choice(option)

# Function to get the index of the computer's choice in the options list
def get_computer_choice_index(choice):
    return option.index(choice)

# Prompt the user to make a choice
print("What do you choose? ")
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Get the names of the user's choice and the computer's choice
user_choice_name = option[user_choice]
computer_choice_name = computer_choice()
computer_choice_index = get_computer_choice_index(computer_choice_name)

# Print the user's choice and its corresponding ASCII art
print("Your choice: ")
print(option_logo[user_choice])

# Print the computer's choice and its corresponding ASCII art
print("Computer choice: ")
print(option_logo[computer_choice_index])

# Determine the outcome of the game and print the result
if user_choice_name == computer_choice_name:
    print("It's a draw!")
elif (user_choice_name == "Rock" and computer_choice_name == "Scissors") or \
     (user_choice_name == "Paper" and computer_choice_name == "Rock") or \
     (user_choice_name == "Scissors" and computer_choice_name == "Paper"):
    print("You win!")
else:
    print("You lose!")