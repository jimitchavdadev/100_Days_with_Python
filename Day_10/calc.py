logo="""
            _            _       _                 
   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | (_| (_| | | (__| |_| | | (_| | || (_) | |  
  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
"""
print(logo)

def mult(first, second):
    return first*second

def div(first, second):
    return first/second

def add(first, second):
    return first+second

def subt(first, second):
    return first-second

operators=['+','-','*','/']

first=float(input("whats the number: "))

result=0

while(True):
    for i in operators:
        print(i)

    op=input("choose an operation: ")
    second=float(input("whats the second number: "))

    if op=="+":
        result=add(first,second)
        print(result)
    if op=="-":
        result=subt(first,second)
        print(result)
    if op=="*":
        result=mult(first,second)
        print(result)
    if op=="/":
        result=div(first,second)
        print(result)

    choice=input("do you want to save the input and perform further or start new operation?\ntype 'yes'  or 'no' or any other key to exit: ")
    if choice=='yes':
        first=result
    elif choice=='no':
        first=float(input("whats the first number: "))
        continue
    else:
        break