import random

print("Welcome to PyPassword Generator")
letters=int(input("how many letters do you want? "))
numbers=int(input("how many numbers do you want? "))
symbols=int(input("How many symbols do you want? "))

letters_list = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

password=""

for i in range(letters):
    password+=random.choice(letters_list)

for i in range(numbers):
    password+=random.choice(numbers_list)

for i in range(symbols):
    password+=random.choice(symbols_list)

password_list=list(password)
random.shuffle(password_list)
final=''.join(password_list)
print("generated password: ",final)