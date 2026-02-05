# Queue Exercises

## Worksheet 1 (Python): Tracing Queue Operations

This worksheet uses a Python list as a queue.

- `enqueue(item)` (in Python, `q.append(item)`): Inserts an element onto the rear.
- `dequeue()` (in Python, `q.pop(0)`): Removes and returns the element at the front.
- `front()` (in Python, `q[0]`): Returns the element at the front without removing it.
- `isEmpty()` (in Python, `len(q) == 0`): Returns `True` if the queue is empty.

**Instructions:** For each problem, trace the operations in the order given. Sketch the final state of the queue `q`, showing the front and rear.

### 1. Basic Trace

A new, empty queue `q` is created.

```python
q = []
q.append(10)  # enqueue
q.append(20)  # enqueue
q.append(30)  # enqueue
q.pop(0)      # dequeue
q.append(40)  # enqueue
```

Final Queue:
(Sketch here, e.g., FRONT -> [ ... ] <- REAR)

### 2. Trace with `front()`

A new, empty queue `q` is created. What is printed to the console?

```python
q = []
q.append("A")  # enqueue
q.append("B")  # enqueue
q.append("C")  # enqueue
print(q[0])     # front
q.pop(0)        # dequeue
print(q[0])     # front
q.append("D")  # enqueue
```

Printed: ______________________

Final Queue:
(Sketch here, e.g., FRONT -> [ ... ] <- REAR)

### 3. Trace with `isEmpty()`

A new, empty queue `q` is created. What is printed to the console?

```python
q = []
print(len(q) == 0)  # isEmpty
q.append(100)       # enqueue
print(len(q) == 0)  # isEmpty
q.pop(0)            # dequeue
print(len(q) == 0)  # isEmpty
```

Printed: ______________________

Final Queue:
(Sketch here, e.g., FRONT -> [ ... ] <- REAR)

### 4. Complex Trace

A new, empty queue `q` is created.

```python
q = []
q.append(5)    # enqueue
q.append(10)   # enqueue
q.append(15)   # enqueue
q.pop(0)       # dequeue
q.append(20)   # enqueue
q.append(25)   # enqueue
q.pop(0)       # dequeue
q.pop(0)       # dequeue
q.append(30)   # enqueue
```

Final Queue:
(Sketch here, e.g., FRONT -> [ ... ] <- REAR)

### 5. Emptying a Queue

A new, empty queue `q` is created. What happens when the last `pop(0)` is called?

```python
q = []
q.append(1)  # enqueue
q.append(2)  # enqueue
q.pop(0)     # dequeue
q.pop(0)     # dequeue
q.pop(0)     # dequeue  # What happens here?
```

Description of last operation: ______________________

Final Queue:
(Sketch here, e.g., FRONT -> [ ... ] <- REAR)

## Worksheet 2 (Python): Algorithmic Queue Problems

**Instructions:** Use loops, if statements, and the fundamental queue operations (`append`, `pop(0)`, `q[0]`, `len(q) == 0`) to solve these problems. You may assume you have a queue `q` (a list) to work with. You may also create one additional temporary queue (`temp = []`) if needed.

### 1. Sum of Queue

Write a function `def sum_queue(q):` that calculates the sum of all integers in the queue. Note: This operation will destroy the original queue (it will be empty after).

```python
def sum_queue(q):
    total_sum = 0
    # Your code here (use a loop and len)

    return total_sum
```

### 2. Count Elements

Write a function `def count(q):` that returns the number of elements in the queue. Crucially, the queue must be in its original state after the function finishes. (Hint: You will need a temporary queue).

```python
def count(q):
    temp = []
    count = 0

    # Your code here to count...

    # Your code here to restore the original queue...

    return count
```

### 3. Find Last Element (Rear)

Write a function `def find_last(q):` that will locate and return the last element added to the queue (i.e., the one at the very rear). The queue must be returned to its original state.

```python
def find_last(q):
    temp = []
    last_element = None

    # Your code here to find the last element and move all items to temp...

    # Your code here to restore the original queue...

    return last_element
```

### 4. Check for Item

Write a function `def exists(q, target):` that returns `True` if the target is in the queue, and `False` otherwise. The queue must be returned to its original state.

```python
def exists(q, target):
    temp = []
    found = False

    # Your code here (check for item, move to temp)

    # Your code here (restore the original queue)

    return found
```

### 5. Get Second Element

Write a function `def get_second_element(q):` that returns the second element from the front of the queue without permanently changing the queue. If the queue has fewer than 2 elements, return `None`.

```python
def get_second_element(q):
    # Your code here (use if, pop(0), q[0], and append)
    return None
```

## Worksheet 3 (Python): Further Problems

1. You are tasked with designing a simple message queue system. This system should allow users to send messages (strings) that are stored in the order they are received. Messages should be retrieved and processed one at a time, in the same order they were sent (FIFO).

   **Requirements:**
   - `enqueue(message)`: Add a new message to the queue.
   - `dequeue()`: Retrieve and remove the oldest message from the queue.
   - `front()`: Get the oldest message without removing it from the queue.
   - `isEmpty()`: Check if the queue is empty.

2. Imagine a scenario like a bank or a store where customers arrive and wait in line to be served. You need to simulate this waiting line using a queue to understand how waiting times and queue lengths change under different conditions (e.g., customer arrival rate, service time).

   **Requirements:**
   - **Customer:** Create a `Customer` class with properties like arrival time and service time.
   - **Queue:** Use a queue (e.g., a list or `collections.deque`) to represent the waiting line.
   - **Simulation:** Simulate the arrival of customers and their service over a period of time.
   - **Metrics:** Track metrics like average waiting time, maximum queue length, and number of customers served.