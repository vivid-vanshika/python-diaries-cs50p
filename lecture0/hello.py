# Day 1 — Greeting Program (CS50P Lecture 0)

def main():
    """Entry point of the program"""
    # Ask for user's name and clean the input
    name = input("What's your name? ").strip().title()

    # Call greeting function with user's name
    hello(name)


def hello(to="world"):
    """Prints a greeting (uses default if no name provided)"""
    print(f"Hello, {to}!")


# Run the program
main()
