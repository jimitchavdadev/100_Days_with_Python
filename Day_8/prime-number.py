def prime_checker(num):
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    print("prime")

print(prime_checker(7))