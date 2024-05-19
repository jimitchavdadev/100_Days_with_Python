import random
from replit import clear

hangman_logo=""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """

words = ["aardvark", "baboon", "camel"]
target_word = random.choice(words)

test_word = ["_"] * len(target_word)
lives = len(test_word)
hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

print(hangman_logo)
print("Welcome to Hangman!")

while lives > 0 and "".join(test_word) != target_word:
    guess = input("Guess a letter: ").lower()
    if guess in target_word:
        print("Good guess!")
        for i in range(len(target_word)):
            if target_word[i] == guess:
                test_word[i] = guess
    else:
        lives -= 1
        print("Wrong guess, lives remaining: " + str(lives))
        print(hangman_stages[len(hangman_stages) - lives - 1])

    print("Current word: " + "".join(test_word))

if "".join(test_word) == target_word:
    print("Congratulations! You guessed the word: " + target_word)
else:
    print("You ran out of lives. The word was: " + target_word)
