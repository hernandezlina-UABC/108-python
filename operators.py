# Arithmetic (basic math)
x = 1
y = 2
res = 0

res = x + y #SUM
print(res)

res = x - y #MINOR
print(res)

res = x * y #MULTIPLICATION
print(res)

res = x / y #DIVISION
print(res)

res = x % y #MODULUS - remainder after division
print(res)

res = x ** y #EXPONENTATION - to the power of
print(res)

res = x // y #FLOOR DIVISION - divides and rops decimal
print(res)

# ASSIGNMENT OPERATON - used to assing values to variables
x = 5
x += 5
x -= 3
x *= 2
x /= 5
print(x)
x += 10
print(x)

#comparison operator - used to compare two values (same as if and else)
'''
== (equals to)
!= (not equal to)
< > (less/greater than)
<= >=(less/greater than or equal to)
'''

#Logical operators - used to combine conditional statements
'''
used with True/False value like conditions
and -> both must be True
or -> at least one must be True
not -> flips True to False (vise versa)
'''

x = 3 
y = 10
z = 10

print(x== y and y ==z) # FALSE, because both condition are NOT true
print(x== y or y ==z) # TRUE, because the second condition (y == z) is true
print(not x==z)     # TRUE, because x != y are not equal


# Identity operator - used to compare objects, not if they're equal but if they're the same object
# is -> check if two thing are the exact same object in memory
# is not -> check if they are NOT the same

x = 3
y = 3
print(x is y) #returns true if both variables are the exact same
print(x is not y) #returns true if both variables are NOT the exact same

#Membership Operator - used to test if a sequence is presented in an object
# in -> check if something exists inside a sequence (list, string... )
# not in -> check if something does NOT exists inside a sequence (list, string... )

x = [1, 2, 3, 4, 5]

print(4 in x) #True, because 4 is inside the list
print(9 not in x) #True, because 9 is NOT inside the list
