import random

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

option = ["Rock", "Paper", "Scissors"]

def computer_choice():
    return random.choice(option)

def get_computer_choice_index(choice):
    return option.index(choice)

print("What do you choose? ")
user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

user_choice_name = option[user_choice]
computer_choice_name = computer_choice()
computer_choice_index = get_computer_choice_index(computer_choice_name)

print("Your choice: ")
print(option_logo[user_choice])
print("Computer choice: ")
print(option_logo[computer_choice_index])

if user_choice_name == computer_choice_name:
    print("It's a draw!")
elif (user_choice_name == "Rock" and computer_choice_name == "Scissors") or \
     (user_choice_name == "Paper" and computer_choice_name == "Rock") or \
     (user_choice_name == "Scissors" and computer_choice_name == "Paper"):
    print("You win!")
else:
    print("You lose!")
