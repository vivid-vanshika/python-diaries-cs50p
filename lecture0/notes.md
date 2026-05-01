# Lecture 0 Notes — Functions, Variables

## Concepts Covered

- **Functions** — reusable blocks of code defined with `def`
- **Parameters & Arguments** — passing data into functions
- **Default Parameters** — `def hello(to="world")` works with or without input
- **Return Values** — functions that give back a result using `return`
- **main()** — entry point function; best practice in Python
- **Variables** — storing values with meaningful names
- **Strings** — text data, manipulated with methods like `.strip()`, `.title()`
- **Formatted Strings (f-strings)** — `f"Hello, {name}!"` for clean output
- **Integers & Floats** — whole numbers vs decimals; use `int()` / `float()` to convert
- **Type Conversion** — `input()` always returns a string; convert before doing math
- **Comments** — `#` for single line, `"""docstring"""` for functions
- **Pseudocode** — planning logic in plain English before writing code
- **Bugs** — errors in logic or syntax; reading error messages carefully helps fix them
- **Readability** — write code for humans first, computers second

---

## Key Insights

**Use main() as the entry point**
```python
def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
# Defining main() and calling it at the bottom is Python best practice
# It keeps input/output logic separate from your other functions
```

**Default parameters make functions flexible**
```python
def hello(to="world"):
    print("hello,", to)

hello()           # → hello, world
hello("Vanshika") # → hello, Vanshika
```

**Always strip and title-case user input**
```python
name = input("What's your name? ").strip().title()
# .strip() removes accidental spaces
# .title() capitalises first letter of each word
```

**Return values let functions give back a result**
```python
def square(n):
    return n * n

print(square(4))  # → 16
```

**f-string formatting tricks**
```python
print(f"{total:,}")      # thousands separator → 1,000,000
print(f"{value:.2f}")    # 2 decimal places   → 3.14
```

**Type conversion is essential for math**
```python
x = float(input("What's x? "))   # input() gives a string, float() makes it a number
```

---

## How My Thinking Evolved

**hello.py** — started with bare `print()` → added a function → added a parameter → added a default parameter → moved input into `main()`

**calculator.py** — started with hardcoded values → moved to user input → added type conversion → added float support → added rounding & formatting → added custom `square()` function with return value

---

## Resources

- [CS50P Lecture 0](https://cs50.harvard.edu/python/2022/weeks/0/)
- [Python f-strings docs](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- [Built-in functions — round(), int(), float()](https://docs.python.org/3/library/functions.html)
