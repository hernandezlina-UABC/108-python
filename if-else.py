'''
A conditional control structure that lts you deccide wich block of code to run 
depending on whether a condition is True or False

if condition:
    - code block runs if condition is True
elif another_condition:
    - code block rund if the first condition is false
    - and this condition is True
else:
    - Code block runs if none of the above conditions are True
'''

x = 7

if x > 0:
    print("x is a positive number")
elif x==0:
    print("x is zero")
else:
    print("x is negative")
    
# Short hand if statements
if x > 5 : print("x is greater than 5")

# Short hand if..else
print("Even") if x % 2 == 0 else print("odd")

# Nested If Statements
if x > 0 :
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions
age = 18

if age>= 15 and age <=21:
    print("You are between 15 and 21")

"""
Mini challenge
1. Ask the user to enter a number from 0-100 and store it in a variable called "score".
2. If the score is 90 or above, print "Grade: A".
3. If the score is between 80-89, print "Grade: B".
4. If the score is between 70-79, print "Grade: C".
5. Otherwise, print "Grade: F".
6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
 BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"
"""
score = int(input("Enter a number from 0-100: "))
if score >=90:
    print("Grade: A")
elif score >=80 and score <=89:
    print("Grade: B")
elif score >=70 and score <=79:
    print("Grade: C")
else:
    print("Grade: F")
if score >=70:
    passed = True
print("Congratulations!") if score >=70 else print("Try again!")


