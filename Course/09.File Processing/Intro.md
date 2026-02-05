# B2.5 — File Processing

This guide introduces **file processing**: reading data from files and writing results back to files.
It’s one of the most practical skills in programming because it connects your code to real-world data.

---

## 1. What is File Processing?

File processing means:

- **Input from files** (instead of only `input()`)
- **Output to files** (saving results so they can be used later)

Most common “real data” formats are just text:

- `.txt` notes and reports
- `.csv` spreadsheet exports
- `.json` saved settings and structured data
- log files (records of events)

---

## 2. File Paths (where your file is)

A very common problem is: *the file exists, but Python says it can’t find it*.
That usually happens because the **current working directory** isn’t the same as the folder the file is in.

In this unit’s exercise file, we use `pathlib.Path` to build reliable paths:

```python
from pathlib import Path

UNIT_DIR = Path(__file__).parent
DATA_DIR = UNIT_DIR / "data"
notes_path = DATA_DIR / "notes.txt"
```

This makes your code work even if you run it from a different folder.

---

## 3. Reading Text Files

### The golden rule: use `with open(...)`

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)
```

Why?

- The file closes automatically.
- Fewer bugs.

### Reading line-by-line (best for large files)

```python
line_count = 0

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # removes the trailing \n
        if line == "":
            continue
        line_count += 1

print("Lines:", line_count)
```

---

## 4. Writing Files (reports and output)

### Write mode (`"w"`)

- Creates the file if it doesn’t exist
- Overwrites the file if it already exists

```python
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Hello file!\n")
    f.write("This is a new report.\n")
```

### Append mode (`"a"`)

- Adds new text to the end
- Does not delete what’s already there

```python
with open("summary.txt", "a", encoding="utf-8") as f:
    f.write("Processed successfully\n")
```

---

## 5. CSV-Style Data (tables in a text file)

CSV is a common way to store table data.
Each line is a row, and commas separate the columns.

Example line:

```text
Steve,85,90,78
```

Basic parsing pattern:

```python
line = "Steve,85,90,78"
parts = line.strip().split(",")

name = parts[0]
math = int(parts[1])
science = int(parts[2])
english = int(parts[3])
```

Important:

- Values start as strings.
- Convert to `int`/`float` when needed.

---

## 6. JSON Data (structured data)

JSON is used for settings and structured lists/dictionaries.
In Python we use the `json` module:

```python
import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

print(students[0]["name"])
```

To save JSON:

```python
with open("students_out.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)
```

---

## 7. Exercise — B2.5 File Processing

Work through the TODOs in the exercise file.
You will read from the files in `data/` and create output files in `output/`.

Run it with:

```bash
python "Course/09.File Processing/file_processing_exercise.py"
```

---

## 8. Common Mistakes (and how to avoid them)

1. **FileNotFoundError**
   - Problem: Wrong path / wrong folder / file name typo
   - Fix: Use `Path(__file__).parent` + check `data/` folder names

2. **Forgetting `.strip()`**
   - Problem: Lines keep the newline `\n`, causing weird comparisons
   - Fix: Use `line = line.strip()` before processing

3. **Not converting numbers**
   - Problem: `"85" + "2"` becomes `"852"` (string join)
   - Fix: Convert with `int(...)` or `float(...)`

4. **Overwriting instead of appending**
   - Problem: Using `"w"` deletes previous contents
   - Fix: Use `"a"` when you want to keep older lines

---

## 9. Practice Problems

1. **Word Frequency:** Read a text file and count the top 10 most common words.

2. **CSV Gradebook:** Read a CSV of student marks, compute averages, and write a report file.

3. **Settings Manager (JSON):** Load settings from JSON, let the user change one value, save it.

4. **Log Analyzer:** Count status codes and top IP addresses from a log file.

---

## Key Takeaways

- Use `with open(...):` for safe file handling.
- Understand file modes: `"r"` read, `"w"` write, `"a"` append.
- Data from files starts as strings — convert types when needed.
- `Path(__file__).parent` helps prevent path issues.
- File processing turns your programs into tools that work with real data.
