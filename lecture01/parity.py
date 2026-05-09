"""x=int(input("what's the value of x? "))
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")"""

# Refactoring the code to use a function to determine if a number is even or odd.

def main():
    x=int(input("what's the value of x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    
 #return True if n%2==0 else False - This is a more concise way to write the same logic using a ternary operator. It is more compact and easier to read.
 #return n % 2 == 0 - This is an even more concise way to write the same logic. It directly returns the result of the expression n % 2 == 0, which will be True if n is even and False if n is odd.

main()
