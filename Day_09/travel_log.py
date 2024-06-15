# Define initial travel_log with sample data
travel_log = [
    {
        "country": "France",
        "visits": 3,
        "cities": ["Paris", "Nice", "Lyon"]
    },
    {
        "country": "Japan",
        "visits": 2,
        "cities": ["Tokyo", "Kyoto"]
    },
    {
        "country": "Italy",
        "visits": 1,
        "cities": ["Rome"]
    }
]

# Loop to allow user to add new logs
while True:
    # Ask user if they want to add a log
    choice = input("Do you want to enter a log? Type 'yes' to add and any other key to exit: ")
    # Check if user wants to add a log
    if choice.lower() == "yes":
        # Get input from user for new log
        country = input("Enter the country you have visited: ")
        visits = int(input("Enter the number of visits: "))
        cities = input("Enter the cities visited (separated by space): ").split()
        # Create new log dictionary
        log = {"country": country, "visits": visits, "cities": cities}
        # Add new log to travel_log list
        travel_log.append(log)
    else:
        # Exit the loop if user does not want to add more logs
        break

# Print the updated travel_log
print(travel_log)