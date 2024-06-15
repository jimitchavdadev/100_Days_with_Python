# Initialize counts for each fur color
gray_count = 0
cinnamon_count = 0
black_count = 0

# Loop through each row in the dataframe
for index, row in data.iterrows():
    # Increment the count based on the fur color
    if row["Primary Fur Color"] == "Gray":
        gray_count += 1
    elif row["Primary Fur Color"] == "Cinnamon":
        cinnamon_count += 1
    elif row["Primary Fur Color"] == "Black":
        black_count += 1

# Create a dictionary to store the counts
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Count the number of squirrels for each fur color using pandas filtering
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

# Create a dictionary with the counts
squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}