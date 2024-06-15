import random

# Welcome message for the PyPassword Generator
print("Welcome to PyPassword Generator")

# Prompt the user to input the number of letters, numbers, and symbols they want in their password
letters = int(input("How many letters do you want? "))
numbers = int(input("How many numbers do you want? "))
symbols = int(input("How many symbols do you want? "))

# Generate lists of possible characters for letters, numbers, and symbols
letters_list = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# Initialize an empty string to hold the password
password = ""

# Add random letters to the password
for i in range(letters):
    password += random.choice(letters_list)

# Add random numbers to the password
for i in range(numbers):
    password += random.choice(numbers_list)

# Add random symbols to the password
for i in range(symbols):
    password += random.choice(symbols_list)

# Convert the password string to a list to shuffle the characters
password_list = list(password)
random.shuffle(password_list)

# Join the shuffled list back into a string to get the final password
final = ''.join(password_list)

# Print the generated password
print("Generated password: ", final)