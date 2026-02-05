# Big O Exercises

**Instructions:** Analyse the following Python code snippets or algorithm descriptions. For each, determine the time complexity and space complexity using Big O notation. Briefly explain your reasoning.

## Part 1: Code Snippets

1. **`print_first_element`**

```python
def print_first_element(my_list):
    """Prints the first element of a list."""
    print(my_list[0])
```

2. **`print_all_elements`**

```python
def print_all_elements(my_list):
    """Prints all elements in a list."""
    for element in my_list:
        print(element)
```

3. **`find_sum`**

```python
def find_sum(my_list):
    """Calculates the sum of all elements in a list."""
    total = 0
    for element in my_list:
        total = total + element
    return total
```

4. **`print_pairs`**

```python
def print_pairs(my_list):
    """Prints all possible pairs of elements in a list."""
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i], my_list[j])
```

5. **`contains_value`** (binary search)

```python
def contains_value(my_list, value):
    """Checks if a sorted list contains a given value using binary search."""
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == value:
            return True
        elif my_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

For each snippet above:

- State the **time complexity** in Big O.
- State the **space complexity** in Big O.
- Give a **one–two sentence explanation**.

## Part 2: Algorithm Descriptions

For each of the following algorithm descriptions, state the time and space complexity and briefly justify your answer:

1. An algorithm that checks if a number is even or odd.
2. An algorithm that finds the smallest element in a sorted list.
3. An algorithm that calculates the factorial of a number `n!`.
4. An algorithm that reverses the order of elements in a list.
5. An algorithm that checks if a string is a palindrome (reads the same backward as forward).
6. An algorithm that generates all possible subsets of a set.
7. An algorithm that finds the closest pair of points in a set of points in a 2D plane (a classic computational geometry problem).

## Part 3: Challenge Questions

1. Consider the following function:

```python
def mystery_function(my_list):
    """Performs a mysterious operation."""
    i = 0
    j = len(my_list) - 1
    while i < j:
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
        i = i + 1
        j = j - 1
```

- What does this function do?
- What are its time and space complexities?

2. An algorithm that finds the second-largest element in an unsorted list.
3. An algorithm that calculates the sum of all the numbers in a 2D array (a list of lists).
4. An algorithm that efficiently searches for a specific value in a sorted tree data structure (you'll learn more about trees later!).
5. An algorithm that finds all the prime numbers less than a given number `n`.

For each of items 2–5, describe a possible algorithm and analyse its time and space complexity.

## Part 4: Scalability and Algorithm Choice

Answer the following conceptual questions. Focus on explaining **why** one complexity might be preferable over another in each scenario.

1. You must write a program to process **millions of financial transactions in real-time**. Would you prefer an algorithm with $O(n^2)$ time complexity or $O(n \log n)$ time complexity? Why?
2. You are designing a mobile app that needs to perform calculations on a **small set of user-provided data**. Does the space complexity of the algorithm matter as much in this scenario compared to the financial transaction processing scenario above? Explain.
3. Describe a situation where you might prioritise using an algorithm with **$O(n)$ time complexity** over an algorithm with **$O(\log n)$ time complexity**, even though $O(\log n)$ is generally more efficient.
4. Why is it important to consider the **scalability** of an algorithm, especially in applications that deal with large and growing datasets?
5. Imagine you are working with a **limited amount of memory**. How might this constraint influence your choice of algorithm?

## Bonus

1. For some of the code snippets or algorithm descriptions above, can you think of **different ways to achieve the same result** with a different Big O complexity?
2. Research and find examples of **real-world applications** where specific Big O notations (e.g., $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$) are crucial for performance.
