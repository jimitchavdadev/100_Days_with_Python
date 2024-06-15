import random

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")

num = random.randint(0, 100)  # Generate a random number between 0 and 100

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set the number of lives based on the difficulty chosen
if diff == "easy":
    lives = 10
else:
    lives = 5

# Game loop
while True:
    print(f"You have {lives} attempts remaining to guess the number.")
    print("Make a Guess: ")

    guess = int(input())  # Get user's guess

    # Check if the guess matches the number
    if guess == num:
        print("You guessed it right!")
        break
    # Provide hints if the guess is too low or too high
    if guess < num:
        print("Too low")
        lives -= 1
    if guess > num:
        print("Too high")
        lives -= 1

    # Check if the player has run out of lives
    if lives == 0:
        print("You ran out of attempts. The number was:", num)
        break