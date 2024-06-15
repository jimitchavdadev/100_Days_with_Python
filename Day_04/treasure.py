# Initialize three lists, each representing a row in a 3x3 grid map
list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

# Combine the three lists into a single list to represent the entire map
map = [list1, list2, list3]

# Prompt the user to input the position where they want to hide the treasure
print("Where do you want to hide your treasure? ")

# Read the position input from the user
position = input()

# Extract the row and column indices from the input and place the treasure symbol '🪙' in the specified location
map[int(position[0])][int(position[1])] = "🪙"

# Print the updated map, showing each row on a new line
print(f"{list1}\n{list2}\n{list3}")