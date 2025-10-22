print("Welcome to Lemon-Tangerine Supermarket!")

user_money = float(input("How many dollars do you have in your wallet?: "))
item = input("What would you like to buy?: ")
item_cost = float(input(f"How much does {item} cost?: "))
money_left_in_wallet = user_money - item_cost
while user_money>item_cost:
    more_items = input("What else would you like?: ")
    item_cost = float(input(f"How much does {more_items} cost?: "))

if user_money>item_cost:
    print ("Money left:" + money_left_in_wallet)
if user_money<item_cost:
    print("Insufficient funds.")

if input == "Done" or "done" or "DONE":
    print("Thank you for shopping.")
    