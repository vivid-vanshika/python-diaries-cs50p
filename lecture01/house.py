# Sorting students into houses based on their names using if-elif-else statements.
'''name=input("what's your name? ")
if name=="Harry":
    print("gryffindor")
elif name=="Hermione":
    print("gryffindor")
elif name=="Ron":
    print("gryffindor")
elif name=="Draco":
    print("slytherin")
else:    
    print("who?")'''

OR

# Using match-case statement
name=input("What's your name? ")
match name:
    case "Harry":
        print("gryffindor")
    case "Hermione":
        print("gryffindor")
    case "Ron":
        print("gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("who?")
           
