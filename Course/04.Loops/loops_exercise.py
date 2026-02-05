"""
1. Create a for loop which uses range() to iterate to 20.
2. Inside the loop, print out the iteration number.
3. Replace the range value to be a user input value. Make sure it's an integer.
4. Add an if statement to check if the iteration number is even or odd.
"""

user_count = int(input("How many iterations?"))
for i in range(1, user_count+1):
    if i % 2 == 0:
        print(f"number {i} is divisible by 2")
    else:
        print(f"number {i} is not divisible by 2")

user_while_count = int(input("What's the max value?"))
counter = 0
while counter <= user_while_count:
    if counter % 2 == 0:
        print(f"number {counter} is divisible by 2")
    else:
        print(f"number {counter} is not divisible by 2")
    counter += 1
