# Conditionals & Flowcharts

This guide explains how to make decisions in Python using `if`, `elif`, and `else`. It also introduces simple flowcharts to plan decision logic. A short exercise (food ordering) is included to practice what you've learned.

---

## 1. When to use conditionals

Conditionals let your program choose different actions depending on values or user input. Use them when the program must react to different situations.

Basic structure:

```python
if condition:
    # code when condition is True
elif another_condition:
    # code when the first is False but this is True
else:
    # code when none of the above conditions hold
```

Example:

```python
age = 15
if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")
```

## 2. Comparison and logical operators

- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`

Example combining conditions:

```python
score = 85
is_member = True
if score > 80 and is_member:
    print("Discount applied")
```

## 3. Flowcharts (simple)

Flowcharts help you plan decision logic before coding. Here are the basic symbols you'll use:

- **Terminator (Ellipse):** Start / End
- **Flowlines (Arrows):** Show the order of steps
- **Input/Output (Parallelogram):** Getting input or printing output
- **Process (Rectangle):** Actions or calculations
- **Decision (Diamond):** A yes/no (True/False) question

![Flowchart Guide Image](image.png)

Quick example (discount flow):

1. Start -> Input cost -> Input membership
2. Decision: cost > 100 and member? -> Yes -> Apply 20% discount -> Print final cost -> End
3. No -> Decision: cost > 100 or member? -> Yes -> Apply 10% discount -> Print final cost -> End
4. No -> No discount -> Print final cost -> End

---

## 4. Exercise — Food ordering (if/elif/else + while)

Practice the conditional logic with a small food-ordering program. The exercise below matches the `03.Conditionals, Flowcharts/elif_exercise.py` in the repository.

Task outline:

1. Create a function `check_calculation()` (no parameters).
2. Ask the user what they want to eat (use `input()`), and convert the response to lowercase.
3. Keep a `total_cost` variable starting at 0.
4. Repeat asking until the user types `"nothing"` or presses Enter without typing anything.
5. If the user types `pizza`, add 10 to `total_cost`.
6. If `burger`, add 7. If `salad`, add 5.
7. If the input doesn't match any of the items, print `Item not recognized`.
8. When the loop ends, print the total cost formatted as currency.

```python
def check_calculation():
    total_cost = 0
    choice = input("What do you want to eat: ").lower()
    while choice != "nothing" and choice != "":
        if choice == "pizza":
            total_cost += 10
        elif choice == "burger":
            total_cost += 7
        elif choice == "salad":
            total_cost += 5
        else:
            print("Item not recognized")
        choice = input("What do you want to eat: ").lower()
    print(f"Total cost: ${total_cost}. Thanks for dining with us!")
```

Hints:

- Test the program by typing `pizza`, `burger`, `salad`, an unknown item, and then `nothing`.

---

## 5. Small practice problems

1. Write a program that asks for a student's grade (0–100) and prints `A`, `B`, `C`, `D`, or `F` using `if`/`elif`/`else`.
2. Create a simple login check: ask for username and password and print `Welcome` or `Access denied`.
