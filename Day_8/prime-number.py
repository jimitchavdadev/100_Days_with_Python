def prime_checker(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    for i in range(2, num):
        if num % i == 0:
            return False  # If the number is divisible by any number other than 1 and itself, it's not prime
    
    return True  # If the loop completes without finding a divisor, the number is prime

# Test the function
num_to_check = 7
if prime_checker(num_to_check):
    print(f"{num_to_check} is prime")
else:
    print(f"{num_to_check} is not prime")