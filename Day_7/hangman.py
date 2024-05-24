import random

logo="""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

stages=[
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

stages=list(reversed(stages))

word_list = [
    "Python",
    "Hangman",
    "Computer",
    "Programming",
    "Game",
    "Developer",
    "Algorithm",
    "Function",
    "Variable",
    "Loop",
    "Condition",
    "Database",
    "Software",
    "Keyboard",
    "Monitor",
    "Internet",
    "Network",
    "Security",
    "Encryption",
    "Artificial"
]

print(logo)

chosen_word=random.choice(word_list)

word_length=len(chosen_word)

lives=6


display=[]
for letter in chosen_word:
    display+="_"
print(display)

end_of_game=False

while (not end_of_game) and display!=chosen_word:
    guess=input("enter the letter: ").lower()

    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")

    if "_" not in display:
        end_of_game=True
        print("You Win!")
    print(stages[lives])
    print(display)

print(f"the user word was {display}")
print(f"the chosen word was {chosen_word}")