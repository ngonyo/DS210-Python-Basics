# Import is like the "include" line in C++
# These lines add a package that our program can use
import sys
import random

# The dot notation represents many things.
# In this case, it says "use this function from package random"
# random.random() returns a number uniformly from [0, 1)
x = random.random()
print(x, type(x))
print()

# Loops work the same way as C++
n = 1
while n <= 10:
    print(random.random())
    n = n + 1

# The range(10) command creates a sequence of integers from [10, 9)
# random.randint(x, y) generates a random integer from [x, y]
print()
for i in range(10):
    x = random.randint(100, 120)
    print(i, x)

print()    
t = ['taco', 'burrito', 'salad', 'vodka']
for i in t:
    print(i)
    
print()
x = 10
while x > 0:
    print(x)
    x = x - 1
print("Crappy New Year!")

print()
for x in range(10):
    print(10-x)
print("Crappy New Year!")

# range(x, y) generates the sequence [x, y)
print()
for x in range(2, 15):
    print(x)
    
# range(x, y, z) generates the sequence [x, y) in steps of z
print()
for x in range(2, 16, 3):
    print(x)
    
print()
for x in range(10, 0, -1):
    print(x)
print("Crappy New Year!")