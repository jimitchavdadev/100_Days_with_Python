# Define the logo for the calculator program
logo = """
            _            _       _                 
   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | (_| (_| | | (__| |_| | | (_| | || (_) | |  
  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
"""
print(logo)  # Print the logo

# Define functions for different operations
def mult(first, second):
    return first * second

def div(first, second):
    return first / second

def add(first, second):
    return first + second

def subt(first, second):
    return first - second

operators = ['+', '-', '*', '/']  # List of available operators

first = float(input("What's the first number: "))  # Get the first number from the user

result = 0  # Initialize the result variable

while True:
    for i in operators:
        print(i)  # Print the available operators

    op = input("Choose an operation: ")  # Get the operator choice from the user
    second = float(input("What's the second number: "))  # Get the second number from the user

    # Perform the selected operation and print the result
    if op == "+":
        result = add(first, second)
        print(result)
    if op == "-":
        result = subt(first, second)
        print(result)
    if op == "*":
        result = mult(first, second)
        print(result)
    if op == "/":
        result = div(first, second)
        print(result)

    # Ask the user if they want to save the result and continue or start a new operation
    choice = input("Do you want to save the result and perform another operation? Type 'yes' or 'no', or any other key to exit: ")
    if choice == 'yes':
        first = result  # Save the result for further operations
    elif choice == 'no':
        first = float(input("What's the first number: "))  # Get a new first number for a new operation
        continue  # Continue to the next iteration of the loop
    else:
        break  # Exit the loop if the user chooses to exit