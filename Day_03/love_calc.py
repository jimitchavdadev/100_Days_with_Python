# Love Calculator

# Print a message indicating that the love score calculation is starting
print("The Love Calculator is calculating your score...")

# Prompt the user to input their name and store the response in the variable name1
name1 = input("What is your name? ")

# Prompt the user to input their partner's name and store the response in the variable name2
name2 = input("What is their name? ")

# Combine both names, convert to lowercase, and store in the variable name3
name3 = (name1 + name2).lower()

# Initialize counters for 'TRUE' and 'LOVE'
Tcount = 0
Lcount = 0

# Loop through each character in the combined names
for i in name3:
    # Check for characters 't', 'r', 'u', 'e' and update Tcount
    if i == 't':
        Tcount += 1
    elif i == 'r':
        Tcount += 1
    elif i == 'u':
        Tcount += 1
    elif i == 'e':
        Tcount += 1
        Lcount += 1  # 'e' contributes to both Tcount and Lcount
    
    # Check for characters 'l', 'o', 'v', 'e' and update Lcount
    elif i == 'l':
        Lcount += 1
    elif i == 'o':
        Lcount += 1
    elif i == 'v':
        Lcount += 1

# Calculate the total love score
total = Tcount * 10 + Lcount

# Provide a response based on the love score
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:  # Corrected the logical condition for the middle range
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")