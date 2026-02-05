# Stack Exercises

## Worksheet 1 (Python): Tracing Stack Operations

This worksheet uses a standard Python list as a stack, which has the following methods:

- `stack.append(item)`: (like push) Inserts an element onto the top of the stack.
- `stack.pop()`: Removes and returns the element at the top of the stack.
- `stack[-1]`: (like peek) Returns the top element without removing it.
- `len(stack) == 0`: (like `isEmpty`) Returns `True` if the stack is empty, else `False`.

**Instructions:** For each problem, trace the operations in the order given. Sketch the final state of the stack `s`. Clearly indicate the top of the stack.

### 1. Basic Trace

A new, empty stack `s` is created.

```python
s = []
s.append(10)
s.append(20)
s.append(30)
s.pop()
s.append(40)
```

Final Stack:
(Sketch here)

### 2. Trace with peek

A new, empty stack `s` is created. What is printed to the console?

```python
s = []
s.append("A")
s.append("B")
s.append("C")
print(s[-1])  # peek
s.pop()
print(s[-1])  # peek
s.append("D")
```

Printed: _________________
Final Stack:
(Sketch here)

### 3. Trace with isEmpty

A new, empty stack `s` is created. What is printed to the console?

```python
s = []
print(len(s) == 0)  # isEmpty
s.append(100)
print(len(s) == 0)  # isEmpty
s.pop()
print(len(s) == 0)  # isEmpty
```

Printed: _________________
Final Stack:
(Sketch here)

### 4. Complex Trace

A new, empty stack `s` is created.

```python
s = []
s.append(5)
s.append(10)
s.append(15)
s.pop()
s.append(20)
s.append(25)
s.pop()
s.pop()
s.append(30)
```

Final Stack:
(Sketch here)

### 5. Emptying a Stack

A new, empty stack `s` is created. What happens when the last `pop()` is called?

```python
s = []
s.append(1)
s.append(2)
s.pop()
s.pop()
s.pop()  # What happens here?
```

Description of last operation: _________________
Final Stack:
(Sketch here)

## Worksheet 2 (Python): Algorithmic Stack Problems

**Instructions:** Use loops, if statements, and the fundamental stack operations (`append`, `pop`, `stack[-1]` for peek, `len(stack) == 0` for `isEmpty`) to solve these problems. You may assume you have a stack (a list) to work with. You may also create one additional temporary stack (`temp = []`) if needed.

### 1. Sum of Stack

Write a function `def sum_stack(s):` that calculates the sum of all integers in the stack. Note: This operation will destroy the original stack (it will be empty after).

```python
def sum_stack(s):
    total_sum = 0
    # Your code here (use a loop and len)
    return total_sum
```

### 2. Count Elements

Write a function `def count(s):` that returns the number of elements in the stack. Crucially, the stack must be in its original state after the function finishes. (Hint: You will need a temporary stack).

```python
def count(s):
    temp = []
    count = 0
    # Your code here to count...
    # Your code here to restore the original stack...
    return count
```

### 3. Find First Pushed (Bottom) Element

Write a function `def find_bottom(s):` that will locate and return (not print) the first element that was pushed onto the stack (i.e., the one at the very bottom). The stack must be returned to its original state.

```python
def find_bottom(s):
    temp = []
    bottom_element = None
    # Your code here to find the bottom element and move all items to temp...
    # Your code here to restore the original stack...
    return bottom_element
```

### 4. Check for Item

Write a function `def exists(s, target):` that returns `True` if the target is in the stack, and `False` otherwise. The stack must be returned to its original state.

```python
def exists(s, target):
    temp = []
    found = False
    # Your code here (check for item, move to temp)
    # Your code here (restore original stack)
    return found
```

### 5. Duplicate Top Element

Write a function `def duplicate_top(s):` that duplicates the top element of the stack. For example, if the stack is `[10, 20, 30]` (with `30` at the top), the result should be `[10, 20, 30, 30]`. If the stack is empty, it should remain empty.

```python
def duplicate_top(s):
    # Your code here (use an if statement and stack[-1])
    pass
```
