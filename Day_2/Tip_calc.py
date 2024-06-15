# Tip Calculator

# Print a welcome message to the user
print("Welcome to the tip calculator!")

# Prompt the user to input the total bill amount and convert the input to a float
bill = float(input("What was the total bill? $"))

# Prompt the user to input the tip percentage they would like to give and convert the input to an integer
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Prompt the user to input the number of people to split the bill and convert the input to an integer
people = int(input("How many people to split the bill? "))

# Calculate the final bill per person by adding the tip to the total bill and then dividing by the number of people
final_bill = (bill * (100 + tip)) / (100 * people)

# Print the final bill per person, rounded to 2 decimal places
print(f"Your final bill is: ${round(final_bill, 2)}")