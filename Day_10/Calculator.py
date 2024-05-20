# Calculator App

import os

logo="""
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
"""

def add(n1, n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "*":multiply,
    "-":subtract,
    "/":divide
}

def calculator():
    print(logo)
    should_continue=True
    num1=float(input("enter the first number: "))
    
    while should_continue:
        num2=float(input("enter the second number: "))

        for symbol in operations:
            print(symbol)

        operation_symbol=input("pick and operation symbol: ")

        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, type 'n' to start new calculation:  ")=="y":
            num1=answer
            os.system("cls")
        else:
            should_continue=False
            os.system("cls")
            calculator()
            
calculator()