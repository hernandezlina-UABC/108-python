'''
Sets are UNORDERED, UNINDEXED, and have no duplicates
created with {}
'''
# RANDOMIZED
fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits)

# Check if item exist
print("banana" in fruits)

# Add Items
fruits.add("orange")
print(fruits)

# Adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# Removing Items
fruits.remove("banana") # Removes item (must exists in the set)
print(fruits)

# If you aren't sure an item exists, use .discard() to avoid any errors
fruits.discard("papaya")
print(fruits)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))     # Combine both (no duplicates)
print(set1.intersection(set2)) # Common elements
print(set1.difference(set2)) # What's unique in set
print(set1.symmetric_difference(set2)) # Everything EXCEPT whats shared (ignores duplicates)

"""
-------------------------------
MINI CHALLENGE: STUDY GROUPS
-------------------------------
Two study groups are preparing for an exam.
"""
# 1. Create two sets:
group_a = {"Lana", "Nina", "Daniel", "Fiona", "Cole"}
group_b = {"Lucy", "Jackson", "Daniel", "Lana", "Jordan", "Harry"}

# 2. Print:
#     - All students participating in either group (union)
print(group_a.union(group_b))    
#     - Students who are in BOTH groups (intersection)
print(group_a.intersection(group_b))    
#     - Students who are only in group_a (difference)
print(group_a.difference(group_b))    
# 3. Add "Maya" to group_a.
group_a.update(["Maya"])
# 4. Remove "Jordan" from group_b.
group_b.remove("Jordan")
# 5. Print the total number of unique students across both groups
both_groups = group_a.union(group_b)
print(len(both_groups))
# 6. If "Nina" is in both groups,
#       print("Nina is helping both groups!")
#    Otherwise,
#       print("Nina is only in one group.")

# 7. Print the final version of both sets.