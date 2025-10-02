# Command Terms

This guide explains common IB command terms you'll see in assessments and exams. Understanding these words helps you know exactly what the question asks for and how to structure your answer.

---

## Quick list of common command terms

- **Define** — Give the precise meaning of a term. Keep it short and accurate.
- **Identify** — Name or select the correct item(s).
- **Describe** — Give details about the topic. Use sentences; include characteristics and features.
- **Explain** — Give reasons or causes. Often requires linking facts with 'because' or 'therefore'.
- **Outline** — Give a brief summary of the main points.
- **Compare** — Show similarities and differences. Use direct comparisons (e.g., "both...", "however...").
- **Contrast** — Focus on differences only.
- **Discuss** — Present a balanced argument with points for and against; give a conclusion.
- **Evaluate** — Judge the value or effectiveness; give reasons and support with evidence, then conclude.
- **Suggest** — Propose a solution or idea; usually short and practical.

---

## How to approach command-term questions

1. Read the command term first, then the full question.
2. Decide how long the answer should be — command terms like `define` need short answers; `discuss` and `evaluate` need longer, structured responses.
3. Use keywords in your answer that match the command term (e.g., when asked to `compare`, use "similar" and "different" or "both" and "however").
4. If asked to `explain` or `evaluate`, include reasons and link statements (because/therefore). For `evaluate`, add a short conclusion.

---

## Examples and model answers

Q: Define "algorithm".

A: An algorithm is a step-by-step set of instructions for solving a problem or performing a task.

Q: Compare arrays and linked lists.

A short model:

- Both arrays and linked lists store collections of elements and can be used to implement lists of items.
- Arrays have fixed size and allow O(1) access by index; linked lists have dynamic size and require O(n) access for random access.
- Arrays can waste space if unused slots exist; linked lists use memory per element but need extra storage for pointers.

Q: Explain why using functions (or procedures) helps with program readability.

A: Functions group related code into named blocks, allowing reuse and hiding implementation details. This reduces repetition and makes the program structure clearer, so readers can understand high-level logic without reading every line.

---

## Command-term examples (repo topics)

Below are short, focused examples using topics we've covered in the repository (variables/data types, operators, strings, loops, conditionals, flowcharts). Use these as models for how to answer command-term questions.

- **Define (data type):**

  Define "integer".

  Model answer: An integer is a whole number without a fractional component, for example 0, 5, or -12.

- **Identify (operators):**

  Identify the operator used for floor division in Python.

  Model answer: The floor division operator is `//`.

- **Describe (string methods):**

  Describe what `replace()` method does for strings.

  Model answer: `replace()` method returns a new string where all occurrences of a specified substring are replaced with another substring; it does not modify the original string.

- **Explain (loops):**

  Explain why a `while` loop might cause an infinite loop.

  Model answer: A `while` loop can become infinite if the loop condition never becomes False because the variables used in the condition are not updated correctly inside the loop.

- **Outline (flowchart):**

  Outline the main steps for a flowchart that calculates a discount based on cost and membership.

  Model answer: Start → Input cost → Input membership → Check conditions for discounts → Apply discount if applicable → Print final cost → End.

- **Compare (conditionals):**

  Compare `if` and `elif` in Python.

  Model answer: `if` starts a conditional block and is evaluated first; `elif` provides additional checks only if previous `if`/`elif` conditions were False. Multiple `elif` blocks can follow an `if`.

- **Contrast (operators):**

  Contrast `/` and `//` in Python.

  Model answer: `/` performs floating-point division and returns a float; `//` performs integer (floor) division and returns an integer when both operands are integers (or a floored float otherwise).

- **Discuss (design choice):**

  Discuss whether using functions for the food-ordering exercise improves the program.

  Model answer: Functions improve readability and reuse; they encapsulate logic (e.g., calculating totals) and make testing easier. However, for very short scripts they add slight overhead and may be unnecessary.

- **Evaluate (method):**

  Evaluate using `input().lower()` for matching user commands in the food-ordering exercise.

  Model answer: Converting input to lowercase simplifies matching and reduces user errors due to capitalization, improving robustness. However, it removes case information if that mattered and could hide intentional differences (rare here).

- **Suggest (improvement):**

  Suggest one improvement to the `elif_exercise` ordering program.

  Model answer: Add a simple menu that shows available items and prices to reduce unrecognized inputs, or validate numeric input for quantities.

---

## Exam tips

- Always answer the exact command term. If the question asks to `outline`, don't provide a long, detailed essay.
- Structure longer answers: short introduction, 2–3 supporting points (with explanations), and a one-line conclusion.
- For `evaluate` and `discuss`, give both sides when appropriate and finish with a judgement.
- Use technical vocabulary and avoid vague phrases like "things" or "stuff".
