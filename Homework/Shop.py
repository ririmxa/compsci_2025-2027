"""
Pure insanity but works somehow
I think i forgot to implement some value error on my script
but who cares
"""

def money(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print("Amount is negative bozo")
                continue
            return value
        except ValueError:
            print("Enter string bozo")

def do_math(amount: float, is_member: bool, threshold: float = 1000.0) -> float:
    member_factor = 1.5
    threshold_factor = 1.1

    if is_member and amount > threshold:
        return amount / threshold_factor / member_factor
    elif is_member and amount <= threshold:
        return amount / member_factor
    elif (not is_member) and amount > threshold:
        return amount / threshold_factor
    else:
        return amount

def main():
    amount = money("What is the value of your basket? ")

    s = input("Are you a store member? True/False? ").strip()
    is_member = (s == "True")

    total = do_math(amount, is_member, threshold=1000.0)

    if amount > 1000:
        print("You are rich maaaaaaaan")
    print(f"Your total cost is: {total:.2f}")

if __name__ == "__main__":
    main()
