# calculator.py — Lecture 0 | CS50P
# Demonstrates: floats, type conversion, f-string formatting, rounding, return values

# --- Addition ---
# float() converts string input to decimal number
# round() rounds to nearest integer
# f"{z:,}" formats with thousands separator e.g. 1,000,000
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"Sum: {z:,}")

# --- Division ---
# f"{z:.2f}" formats to 2 decimal places e.g. 3.14
x = float(input("What's x? "))
y = float(input("What's y? "))
print(f"Division: {x / y:.2f}")

# --- Square (return values) ---
# Functions can return a value using the return keyword
def square(n):
    return n * n

def main():
    x = int(input("What's x? "))
    print("Square of x is", square(x))

main()
