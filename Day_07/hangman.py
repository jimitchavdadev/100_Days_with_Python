import random

# ASCII art for the game logo
logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

# ASCII art for the stages of the game
stages = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Reverse the stages list for correct order during the game
stages = list(reversed(stages))

# List of words for the game
word_list = [
    "Python", "Hangman", "Computer", "Programming", "Game", "Developer",
    "Algorithm", "Function", "Variable", "Loop", "Condition", "Database",
    "Software", "Keyboard", "Monitor", "Internet", "Network", "Security",
    "Encryption", "Artificial"
]

print(logo)  # Print the game logo

# Choose a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6  # Initial lives for the player

# Initialize the display as a list of underscores to represent each letter in the chosen word
display = ["_" for _ in chosen_word]

print(display)  # Print the initial display of underscores

end_of_game = False  # Flag to track game end

# Main game loop
while (not end_of_game) and (display != chosen_word):
    guess = input("Enter a letter: ").lower()  # Get user's guess and convert to lowercase

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Update the display with the guessed letter at the correct positions
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1  # Decrease lives if the guess is incorrect
        if lives == 0:
            end_of_game = True  # End the game if lives reach zero
            print("You Lose")

    # Check if all letters have been guessed correctly
    if "_" not in display:
        end_of_game = True  # End the game if the word is fully guessed
        print("You Win!")

    # Print the current stage of the hangman, display of guessed letters, and remaining lives
    print(stages[lives])
    print(display)

# Print the final result of the game
print(f"The word was: {chosen_word}")
if end_of_game and lives == 0:
    print("Better luck next time!")