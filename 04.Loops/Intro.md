# Loops in Python

This short guide introduces loops in Python. You'll learn when to use `while` and `for` loops and some common pitfalls. Small exercises are included so you can practice.

Link to the presentation: [Loops Presentation](https://www.canva.com/design/DAGzyJv4tcQ/D5H_k_qhHTDkN5tIgqC2Mw/edit?utm_content=DAGzyJv4tcQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## 1. Why use loops?

Loops let you repeat a block of code multiple times without writing it again. Use loops when you need to process many items, repeat an action until a condition changes, or iterate over a sequence.

## 2. The `while` loop

Use `while` when you want to repeat until a condition becomes false.

Example:

```python
count = 0
while count < 5:
    print("count is", count)
    count += 1
```

Notes:

- Make sure the condition will become false eventually. Otherwise you'll create an infinite loop.

Exercise 1 — Sum until stop:

- Write a function that repeatedly asks the user for a number and adds it to a total. The loop should stop when the user types `0` or presses Enter without typing a number. Print the final total.

## 3. The `for` loop

Use `for` when you want to repeat an action a specific number of times or iterate over a sequence of numbers.

Example (range):

```python
for i in range(3):  # 0, 1, 2
    print(i)
```

Notes:

- `range(start, stop, step)` produces a sequence of numbers. `range(n)` is the same as `range(0, n)`.

Exercise 2 — Count down:

- Write a function that asks the user for a number `n` and prints numbers from `n` down to 1 using a `for` loop and `range()`.

## 4. Advanced (covered later)

Topics such as `break`, `continue`, and nested loops are useful, but they will be introduced later in the course. For now, focus on writing clear `while` and `for` loops and solving the practice problems.

## 6. Common pitfalls & tips

- Infinite loops: ensure loop conditions change.
- Off-by-one errors with `range()` (remember `stop` is excluded).
- Avoid modifying the list you're iterating over; iterate over a copy instead: `for x in my_list[:]`.
- Keep loops small and simple, move complex logic into functions.

## 7. Small practice problems

1. Write a program that prints all prime numbers less than 30.
2. Create a loop that asks for names until the user types "done"; then print the list of names.
3. Given a list of student scores, use a loop to compute the average score.
