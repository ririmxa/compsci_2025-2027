# Scope and Functions

This guide introduces two fundamental programming concepts: variable scope and functions. You'll learn how to organize your code into reusable blocks and understand where variables can be accessed in your programs. Practical exercises are included to reinforce these concepts.

---

## 1. What is Scope?

Scope determines where variables can be accessed and modified in your program. Understanding scope helps prevent errors and makes your code more predictable.

### Types of Scope

- **Local scope:** Variables defined inside a function, only accessible within that specific function
- **Enclosing scope:** Variables in the local scope of enclosing functions (for nested functions)
- **Global scope:** Variables defined outside any function, accessible throughout the entire program
- **Built-in scope:** Python's built-in names like `print`, `len`, `input`

Example:

```python
name = "Alice"  # Global variable

def outer_function():
    message = "Hello"  # Enclosing scope variable
    
    def inner_function():
        greeting = "Hi"  # Local variable
        print(f"{greeting}, {message}, {name}!")  # Can access local, enclosing, and global
    
    inner_function()
    print(f"{message}, {name}!")  # Can access enclosing (message) and global

def farewell():
    print(f"Goodbye, {name}!")  # Can access global
    # print(message)  # ERROR: Cannot access enclosing variable from different function

outer_function()  # Output: Hi, Hello, Alice! 
                  #         Hello, Alice!
farewell()        # Output: Goodbye, Alice!
```

### The `global` Keyword

Sometimes you need to modify a global variable inside a function:

```python
counter = 0  # Global variable

def increment():
    global counter
    counter += 1
    print(f"Counter is now: {counter}")

increment()  # Counter is now: 1
increment()  # Counter is now: 2
```

**Important:** Avoid using `global` whenever possible. It makes code harder to understand and debug.

## 2. Functions

Functions are reusable blocks of code that perform specific tasks. They help organize your program into logical sections and avoid code repetition.

### Basic Function Structure

```python
def function_name(parameters):
    """Optional docstring explaining what the function does"""
    # Function body
    return value  # Optional return statement
```

### Functions Without Parameters

```python
def say_hello():
    print("Hello, World!")

say_hello()  # Output: Hello, World!
```

### Functions With Parameters

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8
```

### Functions With Default Parameters

```python
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_user("Alice"))           # Output: Hello, Alice!
print(greet_user("Bob", "Hi"))       # Output: Hi, Bob!
```

### Return Values

Functions can return values using the `return` statement:

```python
def calculate_area(length, width):
    area = length * width
    return area

room_area = calculate_area(10, 12)
print(f"Room area: {room_area} square meters")
```

**Note:** If no `return` statement is used, the function returns `None`.

## 3. Scope Within Functions

Variables created inside functions are local to that function:

```python
def calculate_total(price, tax_rate):
    tax = price * tax_rate  # Local variable
    total = price + tax     # Local variable
    return total

final_cost = calculate_total(100, 0.08)
print(final_cost)  # Output: 108.0
# print(tax)  # ERROR: 'tax' is not accessible outside the function
```

### Variable Shadowing

Local variables can "shadow" (hide) global variables with the same name:

```python
x = "global"

def demo():
    x = "local"  # This shadows the global x
    print(f"Inside function: {x}")

demo()           # Output: Inside function: local
print(f"Outside function: {x}")  # Output: Outside function: global
```

## 4. Best Practices

1. **Use descriptive function names:** `calculate_discount()` instead of `calc()`
2. **Keep functions small:** Each function should do one thing well
3. **Use parameters instead of global variables:** Makes functions more reusable
4. **Document your functions:** Use docstrings to explain what they do
5. **Return values instead of printing:** Makes functions more flexible

Example of good function design:

```python
def calculate_discount(price, discount_percent):
    """
    Calculate the discount amount and final price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)
    
    Returns:
        tuple: (discount_amount, final_price)
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return discount_amount, final_price

# Usage
original = 200
discount, final = calculate_discount(original, 15)
print(f"Original: ${original}, Discount: ${discount}, Final: ${final}")
```

---

## 5. Exercise — Library Management System

Practice scope and functions with a simple library management program.

**Task:** Create functions to manage a library's book collection.

Requirements:

1. Create a global list `books` to store book titles
2. Write a function `add_book(title)` that adds a book to the collection
3. Write a function `remove_book(title)` that removes a book from the collection
4. Write a function `list_books()` that displays all books
5. Write a function `book_count()` that returns the number of books
6. Create a main function that provides a simple menu interface

```python
# Global variable to store books
books = []

def add_book(title):
    """Add a book to the library collection."""
    books.append(title)
    print(f"'{title}' has been added to the library.")

def remove_book(title):
    """Remove a book from the library collection."""
    if title in books:
        books.remove(title)
        print(f"'{title}' has been removed from the library.")
    else:
        print(f"'{title}' not found in the library.")

def list_books():
    """Display all books in the library."""
    if books:
        print("Books in the library:")
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
    else:
        print("The library is empty.")

def book_count():
    """Return the number of books in the library."""
    return len(books)

def main():
    """Main function to run the library management system."""
    while True:
        print("\n--- Library Management ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. List books")
        print("4. Book count")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            add_book(title)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            remove_book(title)
        elif choice == "3":
            list_books()
        elif choice == "4":
            count = book_count()
            print(f"Total books: {count}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
```

**Extension:** Modify the program to avoid using global variables by passing the `books` list as a parameter to each function.

---

## 6. Common Mistakes and How to Avoid Them

1. **Using global variables unnecessarily**
   - Problem: Makes code hard to test and debug
   - Solution: Pass data as parameters and return results

2. **Forgetting to return values**
   - Problem: Functions that should return values return `None`
   - Solution: Always use `return` when you need a result

3. **Modifying global variables accidentally**
   - Problem: Unexpected changes to global state
   - Solution: Use local variables and parameters

4. **Functions that are too long**
   - Problem: Hard to understand and maintain
   - Solution: Break large functions into smaller ones

---

## 7. Practice Problems

1. **Temperature Converter:** Write functions to convert between Celsius, Fahrenheit, and Kelvin.

2. **Password Validator:** Create a function that checks if a password meets certain criteria (length, uppercase, lowercase, digits).

3. **Shopping Cart:** Build functions to add items, remove items, calculate totals, and apply discounts to a shopping cart.

4. **Grade Calculator:** Write functions to calculate letter grades, GPA, and class averages from a list of scores.

---

## Key Takeaways

- **Scope** determines where variables can be accessed in your program
- **Functions** help organize code into reusable, logical blocks
- **Local variables** exist only within their function
- **Global variables** should be used sparingly
- **Good function design** makes code easier to read, test, and maintain
- **Parameters and return values** make functions flexible and reusable
