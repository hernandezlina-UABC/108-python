'''
A for loop in Python is a control structure that lets you repeat
a block of code each item in a sequence

for variable in sequence:
    # Code block runs for each item in the sequence
'''

# Loop through a list
list = ["apple", "banana", "cherry"]
for fruit in list:  # for each fruit (item) in the list
    print(fruit)
print("------------------------------------------")

# Loop through a string
for letter in "Hello":
    print(letter)
print("------------------------------------------")

# Loop Methods
# range() generates a sequence of numbers
# (start, stop, step) step - skip over
for x in range(5): # When only one number starts at 0 to the end
    print(x)
print("------------------------------------------")

# Start and End the range
for x in range(2,6): #2-5
    print(x)
print("------------------------------------------")

for x in range(0, 10, 2): #0-10 skip 2
    print(x)
print("------------------------------------------")

#Else in for loop
for x in range(3):
    print(x)
else:
    print("Loop Done!")
print("------------------------------------------")

# BREAK and CONTINUE
for x in range(10):
    if x == 5:
        continue    # skips 5
    if x == 8:
        break       # stops loop at 8
    print(x)
print("------------------------------------------")

# Nested for loops
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()
    
# MINI-CHALLENGE
# 1. ask the user to enter a number and store it in a variable valled num
num = int(input("Enter a number: "))
# 2. use a for loop with range (1,11) to repeat 10 times
for i in range(1, 11):

# 3. inside the loop, multiple num by the current loop value (i)
#       f"num X i = num * i"
    print(f"{num} X {i} = {num * i}")



 


