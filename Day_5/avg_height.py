height = [170, 165, 180, 175, 160]  # Example list of heights

# Initialize sum to zero
sum_height = 0

# Calculate the sum of heights
for h in height:
    sum_height += h

# Calculate the average height
if len(height) > 0:
    average_height = sum_height / len(height)
    print(f"The average height is: {average_height}")
else:
    print("The height list is empty.")