'''
Tuples are IMUTABLE (you can't change them after creation)
Created with ( )
'''

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing Items
print(my_tuple[1])
print(my_tuple[-1])

# Checking if item exists
if "apple" in my_tuple:
    print("Yes")

# Single Item Tuples
# You must add a comma at the end or Python wint recognize it as a tuple
single = ("apple",)     # Tuple
print(type(single))
not_tuple = ("apple")   # String
print(type(not_tuple))

# Nested Tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

# COUNT and INDEX (the two method tuples DO have)
letters = ("a", "b", "a", "c", "d", "a")
print(letters.count("a")) # counts how many times "a" appears in tuple
print(letters.index("c")) # The index where "c" first appears

# Tuple Unpacking
# you can "unpack" tuple items directly into separete variables
coordinates =  (10, 20)
x, y = (coordinates)
print(x)
print(y)

person = ("Leo", 22, "Computers")
name, age, hobbies = person
print(f"{name} is {age} years old and his hobbie is {hobbies}")

"""
-------------------------------
MINI CHALLENGE: THE TRAVEL BAG
-------------------------------
You’re packing for a trip! You have a tuple that stores the items you’re taking.
"""
# 1. Create a tuple called "travel_bag" with at least 5 items (e.g. "shirt", "toothbrush", etc.)
travel_bag = ("toothpaste", "shirt", "skirt", "jeans", "jacket")
# 2. Print the SECOND and FOURTH items in your bag.
print(travel_bag[1])
print(travel_bag[3])
# 3. Check if "shoes" is in your travel bag — if it is, print "You're ready to walk!"
#     otherwise, print "You forgot your shoes!"
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# 4. Make a new tuple called "essentials" with 3 must-have items.
essentials = ("shampoo", "kleenex", "ibuprofen")
# 5. Combine both tuples into one called "final_bag".
final_bag = travel_bag + essentials
# 6. Print how many total items you now have using len().
print(len(final_bag))
# 7. Print the last item in your "final_bag".
print(final_bag[-1])