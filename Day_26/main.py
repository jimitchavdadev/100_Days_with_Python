import pandas  # Import pandas for data handling

# Read the NATO phonetic alphabet data from a CSV file into a DataFrame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to their phonetic codes using dictionary comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask the user to input a word and convert it to uppercase
user_word = input("Enter a word: ").upper()

# Convert each letter in the input word to its corresponding phonetic code using list comprehension
output = [phonetic_dict[letter] for letter in user_word]

# Print the phonetic codes for the input word
print(output)