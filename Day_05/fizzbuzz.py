target = 15  # Example target value

# Loop from 0 to target (inclusive)
for i in range(0, target + 1):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)