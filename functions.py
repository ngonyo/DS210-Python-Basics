import sys

# This program will show you the basics of function
# syntax in Python.

def lumberjack():
    print("I'm a lumberjack and I'm ok.")
    print("Sleep all night and work all day.")
    print("I'm a lumberjack, but actually I'm not ok.")
    print("This function is a cry for help.")
    print("Help.")
    print("My name is Roy Sullivan.")

def printtwice(lightning):
    print(lightning)
    print(lightning)

def creepcalculator(yourage, theirage):
    # True means you're a creep
    if yourage/2 + 7 > theirage:
        return True
    return False
    # This function represents short circuit logic
    # You do not have to explicitly write "else" because
    # You KNOW that when you get to line 22, you are not
    # a creep

print("Hi!")
lumberjack()
printtwice("fish")
print(creepcalculator(40, 20))
try:
    print(creepcalculator(int(sys.argv[1]), int(sys.argv[2])))
except:
    print("Usage: python3 functions.py <int> <int>")
