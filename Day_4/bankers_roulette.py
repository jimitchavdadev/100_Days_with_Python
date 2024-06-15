import random

# Prompt the user to input a list of names, separated by spaces, and store the response in names_string
names_string = input("Enter the names of people (separated by spaces): ")

# Split the names_string into individual names and store them in a list named names
names = names_string.split(" ")

# Use the random.choice() function to randomly select a name from the list
payer = random.choice(names)

# Print the name of the person who will pay for the meal
print(f"{payer} is going to pay for the meal today")