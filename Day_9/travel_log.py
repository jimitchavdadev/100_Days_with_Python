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

while(True):
    choice=input("do you want to enter a log? type 'yes' to add and other key to exit: ")
    if choice=="yes":
        country=input("enter the country you have visited: ")
        visits=int(input("enter the number of visits: "))
        cities=input("number of cities: ")
        cities=cities.split(" ")
        log={"country":country,"visits":visits,"cities":cities}
        travel_log.append(log)
    else:
        break

print(travel_log)
