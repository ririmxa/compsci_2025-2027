"""
Take user input and store it as integer in a variable
assign a total value variable to track the total
Write a for loop that adds all the numbers from 1 to user input using range()
print the total value at the end
"""

user_input = int(input())

total_value = 0

for i in range (1, (user_input + 1)):
	total_value += i

print(total_value)


