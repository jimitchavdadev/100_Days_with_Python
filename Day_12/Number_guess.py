import random

print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")

num=random.randint(0,100)

diff=input("choose a difficulty. Type 'easy' or 'hard': ")

lives=0
if diff=="easy":
    lives=10
else:
    lives=5

while(True):
    print(f"you have {lives} attempts remaining to guess the number.")
    print("Make a Guess: ")

    guess=int(input())

    if guess==num:
        print("you guessed it right!")
        break
    if guess<num:
        print("too low")
        lives=lives-1
    if guess>num:
        print("too high")
        lives=lives-1

