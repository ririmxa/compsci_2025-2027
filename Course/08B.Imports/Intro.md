# B2.x — Imports in Python

This guide introduces **imports**: how Python uses code from other modules (files), packages (folders), and the standard library.
Imports are how we avoid rewriting the same code and how we use powerful built-in tools.

---

## 1. What is an import?

An `import` lets you use code that lives somewhere else:

- **Standard library** modules (come with Python): `math`, `random`, `json`, `pathlib`, `datetime`, …
- **Your own modules**: other `.py` files you wrote
- **Third-party packages** (installed with pip): not covered in depth yet

---

## 2. Modules vs packages

- A **module** is a single Python file (example: `my_utils.py`).
- A **package** is a folder of modules (usually with an `__init__.py` inside).

For now, we’ll focus on modules.

---

## 3. Common import styles

### Import the whole module

```python
import math

print(math.sqrt(16))
print(math.pi)
```

### Import specific names from a module

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

### Aliases (shorter names)

```python
import random as rnd

print(rnd.randint(1, 6))
```

---

## 4. Importing your own code (local modules)

If you have a file in the same folder, like `my_utils.py`, you can import it:

```python
import my_utils

print(my_utils.shout("hello"))
```

Important rules:

- The file name becomes the module name: `my_utils.py` → `import my_utils`
- You usually **should not** name your file the same as a standard library module.
  - Bad: `random.py`, `json.py`, `math.py`

---

## 5. Where Python looks for modules (the path)

Python searches for modules in:

1. The folder of the script you are running
2. The current working directory
3. The Python installation and site-packages

If an import fails, it’s usually because the file is not where Python is looking.

---

## 6. Exercise — Imports

Open `imports_exercise.py` and complete the TODO sections.

Run it with:

```bash
python "Course/08B.Imports/imports_exercise.py"
```

---

## 7. Common mistakes (and how to avoid them)

1. **`ModuleNotFoundError`**
   - Problem: The module isn’t in the same folder (or not installed)
   - Fix: Check spelling, file location, and run the script from the correct place

2. **Shadowing a library module**
   - Problem: Naming your file `random.py` and then `import random`
   - Fix: Rename your file (e.g. `random_demo.py`) and delete `__pycache__` if needed

3. **Circular imports**
   - Problem: `a.py` imports `b.py` and `b.py` imports `a.py`
   - Fix: Move shared code to a third file (e.g. `ab.py`) or redesign dependencies

---

## Key Takeaways

- Imports let you reuse code from Python, libraries, and your own files.
- `import module` uses `module.name` to access things.
- `from module import name` imports specific names directly.
- File names matter: `thing.py` imports as `import thing`.
