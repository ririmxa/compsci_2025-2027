"""
Find the errors in the code on your own.
Try to fix the errors FIRST USING "global" keyword, write comments to describe the errors.
Use breakpoints and print() calls to see if it functions as it should. (15 mins)
If you finish early, try to also solve the bugs by removing the global variable and using parameters and return values.
Discuss your code in pairs and explain your reasoning to each other (10 mins)
We'll go over the errors together after the exercise to see where you may have had problems
THINGS TO CONSIDER :
    1: Can you explain what the function does without showing the code itself?
    2: Did you avoid using global variables as much as you can?
    3: Are your function and variable names descriptive and concise?
    4: Do your comments describe the functionality well enough?
"""



balance = 1000

def deposit(amount):
    balance = balance + amount
    print("Deposited", amount, "New balance:", balance)

def withdraw(amount):
    if balance >= amount:
        balance = balance - amount
        print("Withdrew", amount, "New balance:", balance)
    else:
        print("Insufficient funds!")

def bank_app():
    print("Welcome to your bank account!")
    deposit(200)
    withdraw(150)
    withdraw(1200)
    print("Final balance:", balance)

bank_app()