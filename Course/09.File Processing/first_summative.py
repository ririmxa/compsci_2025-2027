def shopping():
    purchases = []
    """
    Loop for getting the wallet value until "done"
    """
    while True:
        pocket = input("How much money do you have in your pocket? ").strip()
        if pocket.lower() == "done":
            print("You don't have money to spend.")
            return
        try:
            pocket_balance = float(pocket)  # We need to convert to number for calculations
            if pocket_balance < 0:
                print("Amounts can't be negative")
                continue
            break
        except ValueError:
            print("Please enter the valid numbers")

    total_spent = 0.0 # Tracking variable

    """
    Main loop for shopping
    """
    while True:
        item_name = input("What would you like to buy? ").strip()
        #  Stop word "done"
        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Please enter an item name.")
            continue

        # Ask for item's price as input
        price_input = input("How much does it cost? ").strip()
        if price_input.lower() == "done":
            break  # allow stopping here too
        try:
            item_cost = float(price_input) # convert to float data-type for calculations
            if item_cost <= 0:
                print("Please enter a positive prices")
                continue
        except ValueError:
            print("Enter a valid number plz")
            continue

        """
        Conditional check for checking if we can afford it or not
        """
        if item_cost <= pocket_balance:
            # Update wallet, and total cost
            pocket_balance -= item_cost
            total_spent += item_cost
            print(f"{item_name} was purchased for {item_cost}PLN. "
                  f"You have {pocket_balance}PLN left.")
            purchases.append((item_name, item_cost)) # Add the purchase to the list
            # If money is gone and is 0 you get break.
            if pocket_balance == 0:
                print("You have run out of money.")
                break
        else:
            # Not affordable, so print warnings
            print(f"You don't have enough money to afford {item_name}.")
            print(f"You still have {pocket_balance}PLN left.")

    # Summary on your shopping
    print(f"Shopping complete. You have {pocket_balance}PLN remaining in your wallet, "
          f"you’ve spent {total_spent}PLN.")

if __name__ == "__main__":
    shopping()


