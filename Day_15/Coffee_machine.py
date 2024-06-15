logo="""
 ██████  ██████  ███████ ███████ ███████ ███████        
██      ██    ██ ██      ██      ██      ██             
██      ██    ██ █████   █████   █████   █████          
██      ██    ██ ██      ██      ██      ██             
 ██████  ██████  ██      ██      ███████ ███████        
                                                        
                                                        
███    ███  █████   ██████ ██   ██ ██ ███    ██ ███████ 
████  ████ ██   ██ ██      ██   ██ ██ ████   ██ ██      
██ ████ ██ ███████ ██      ███████ ██ ██ ██  ██ █████   
██  ██  ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██      
██      ██ ██   ██  ██████ ██   ██ ██ ██   ████ ███████ 
"""

# Menu of available drinks with their ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Function to print the current resources status
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

# Function to check if there are enough resources to make the selected drink
def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coins and calculate the total amount inserted
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

# Function to check if the transaction is successful and provide change if needed
def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the selected drink and update resources
def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")

# Main function to operate the coffee machine
def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                payment = process_coins()
                if check_transaction(payment, MENU[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please try again.")

# Start the coffee machine
print(logo)
coffee_machine()