"""
A simple food ordering system that calculates the total cost based on user input.
The user can order pizza, burger, or salad. The loop continues until the user types
"nothing" or presses enter without typing anything.
"""
# 1. Write a check_calculation function without parameters
# 2. Assign a variable that stores user input that is converted to all lowercase.
# 3. Assign a total_cost variable with the initial value 0.
# 4. Write a while loop that checks if input is "nothing" or "" to exit the loop.
# 5. Create if/elif checks to see if the input matches food items (e.g., "pizza", "burger", "salad").
# 6. Assign prices to each food item (e.g., pizza = 10, burger = 7, salad = 5).
# 7. If the input matches a food item, add its price to the total_cost variable.
# 8. If the input doesn't match any food item, print "Item not recognized".

def check_calculation():
    """Calculates the total cost of food items ordered by the user."""
    total_cost = 0
    myvalue = input("What do you want to eat: ").lower()
    # while loops are explained in the next week's material
    while myvalue != "nothing" and myvalue != "":
        if myvalue == "pizza":
            total_cost += 10
            print("Yum yum yum")
        elif myvalue == "burger":
            total_cost += 7
            print("Yum yum yum")
        elif myvalue == "salad":
            total_cost += 5
            print("Yum yum yum")
        else:
            print("Item not recognized")
        myvalue = input("What do you want to eat: ")
    print(f"Total cost: ${total_cost}. Thanks for dining with us!")
