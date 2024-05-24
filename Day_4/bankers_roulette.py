import random

names_string=input("enter the name of people: ")
names=names_string.split(" ")
print(f"{random.choice(names)} is going to pay for the meal today")