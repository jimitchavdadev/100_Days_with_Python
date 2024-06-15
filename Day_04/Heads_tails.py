import random

# List containing the two possible outcomes of a coin flip
option = ["Heads", "Tails"]

# Use random.choice to randomly select either "Heads" or "Tails" from the option list
result = random.choice(option)

# Print the result of the coin flip
print(f"You got {result}")