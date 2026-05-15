"""i=4
while i!=0:
    print("meow")
    i=i-1"""

"""i=0
while i<=5:
    print("meow")
    i+=1"""


"""for i in range(5):
    print("meow") """

# The _ is used as a throwaway variable when we don't need to use the loop variable. It indicates that we are not interested in the value of the loop variable and just want to repeat the block of code a certain number of times.
"""for _ in range(5):
    print("meow")"""

# print("meow\n" * 3, end="")

# The code below prompts the user to enter a positive integer value for n. It uses a while loop to repeatedly ask for input until a valid positive integer is entered. Once a valid n is obtained, it uses a for loop to print "meow" n times.
"""while True:
    n= int(input("What's the value of n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")"""



"""def main():
    number=getdef main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()"""


# def function
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("what's the value of n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


