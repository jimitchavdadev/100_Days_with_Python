marks = [87, 92, 78, 85, 90]  # Example list of marks

# Initialize max_mark to the first mark in the list
max_mark = marks[0]

# Iterate through the list to find the maximum mark
for mark in marks:
    if mark > max_mark:
        max_mark = mark  # Update max_mark if a larger mark is found

print(max_mark)  # Print the maximum mark