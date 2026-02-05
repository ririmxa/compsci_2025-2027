# B2.x — Exception Handling (try/except)

This guide introduces **exception handling**: how to prevent your programs from crashing when something goes wrong.
In real programs, errors happen (bad input, missing files, invalid numbers). Good programs handle them safely.

---

## 1. What is an exception?

An **exception** is an error that happens while the program is running.
If you don’t handle it, Python stops your program and prints a traceback.

Examples:

- `ValueError` when converting text to a number
- `ZeroDivisionError` when dividing by 0
- `IndexError` when you access a list index that doesn’t exist (example: `items[10]` when the list is shorter)
- `TypeError` when you use the wrong type in an operation (example: `"5" + 2`)
- `NameError` when you use a variable name that doesn’t exist (usually a typo)
- `AttributeError` when you try to use a method/attribute that doesn’t exist for that type
- `ModuleNotFoundError` when Python can’t find a module you tried to import (We learned about imports on Tuesday)
- `FileNotFoundError` when a file path does not exist (we'll talk about it next semester at File Processing)
- `KeyError` when a dictionary key is missing (short intro about dictionaries)

---

## 2. Basic try/except

Use `try/except` to run code that might fail.

```python
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a valid integer.")
```

What this does:

- If conversion works, `except` is skipped.
- If conversion fails, Python jumps into the `except` block instead of crashing.

---

## 3. Handling multiple exceptions

```python
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ValueError:
    print("Please enter integers only.")
except ZeroDivisionError:
    print("You can't divide by zero.")
```

---

## 4. else and finally

`else` runs only if there was no exception.
`finally` runs no matter what (success or error).

```python
try:
    x = int(input("x: "))
except ValueError:
    print("Invalid input")
else:
    print("Valid number:", x)
finally:
    print("This always runs.")
```

---

## 5. When NOT to use exceptions

Exception handling is for **unexpected problems**, not for normal logic.
For example, don’t use exceptions to control a normal loop.

Better:

- Use `if` checks when you can (like checking list length)
- Use exceptions when you cannot predict everything (file missing, user enters letters)

---

## 6. Exercise — Exception Handling

Open `exception_handling_exercise.py` and complete the TODOs.

Run it with:

```bash
python "Course/08C.Exception Handling/exception_handling_exercise.py"
```

---

## 7. Common mistakes (and how to avoid them)

1. **Catching everything with `except:`**
   - Problem: It hides real bugs.
   - Fix: Catch specific exceptions like `ValueError` and `FileNotFoundError`.

2. **Putting too much code in the try block**
   - Problem: You don’t know which line failed.
   - Fix: Keep the `try` block small.

3. **Swallowing errors silently**
   - Problem: You lose information.
   - Fix: Print a helpful message or re-raise when appropriate.

---

## Key Takeaways

- Exceptions prevent crashes when unexpected things happen.
- Use `try/except` to handle specific errors safely.
- `else` runs on success; `finally` runs always.
- Keep `try` blocks small and focused.
