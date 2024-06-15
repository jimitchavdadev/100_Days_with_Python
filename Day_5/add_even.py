# Initialize target value and sum accumulator
target = 0
sum = 0

# Loop through all even numbers from 0 to the target (inclusive)
for i in range(0, target + 1, 2):
    sum += i  # Add the current even number to the sum

# Print the final sum of all even numbers up to the target
print(sum)