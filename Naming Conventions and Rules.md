# Python Naming Conventions and Rules (PEP 8)

PEP 8 is the official style guide for Python code. Following these conventions makes your code readable and consistent.

---

## Variable Names

- Use lowercase letters and underscores: `my_variable`
- Avoid single-character names except for counters: `i`, `j`
- Be descriptive: `total_price` is better than `tp`

## Function Names

- Use lowercase letters and underscores: `calculate_total()`
- **DO NOT PLACE SPACES BETWEEN FUNCTION NAMES AND THE PARENTHESES**
- Function names should describe what they do

## Class Names

- Use CapitalizedWords (PascalCase): `MyClass`, `StudentRecord`

## Constant Names

- Use all uppercase letters with underscores: `MAX_SIZE`, `PI`
- Constants are usually defined at the top of a python file to indicate they should not be changed.

---

## General Rules

- No spaces in names
- Avoid starting names with numbers
- Do not use Python keywords as names (e.g., `class`, `def`, `if`)
- Use meaningful names that describe the purpose

---

## Escape Characters

If we want to add special characters in a string, we can use escape characters.
Otherwise, the string will end at the special character which will most likely cause an error.
Escape characters are used to represent special characters in strings.

Common examples include:

- `\n` for newline
- `\t` for tab
- `\\` for backslash
- `\"` for double quote
- `\'` for single quote

Use escape characters to include special formatting or symbols in your strings.

## Examples

```python
# Variable
student_name = "Alice"

# Function
def calculate_average(score_list):
    ...

# Class - Will be discussed later
class StudentRecord:
    ...

# Constant
MAX_SCORE = 100


# Escape characters in strings
escaped_quote = "She said, \"Hello!\""
# Will print out She said, "Hello!"
escaped_newline = "Line1\nLine2"
# Will print out:
# Line1
# Line2
escaped_tab = "Column1\tColumn2"
# Will print out Column1    Column2
escaped_backslash = "C:\\path\\to\\file"
# Will print out C:\path\to\file
```

---

For more details, see the [PEP 8 documentation](https://peps.python.org/pep-0008/#naming-conventions).
