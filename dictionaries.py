'''
Dictionaries store data in KEY: VALUE pairs
Written with { }
'''

students = {
    "name": "Lina",
    "age": "25",
    "major": "Software Development"
}
print(students)

#ACCESSING items
print(students["name"])
print(students.get("major"))

# Adding new items
students["graduation_year"] = 2028
print(students)

# Changing values
students["age"] = 21
print(students)

# Removing items
students.pop("major") # removes "major"
print(students)

# Check if KEY exists
if "name" in students:
    print("Yes, 'name' is in the dictionary")

# Nested Dictionary
student = {
    "student1": {"name": "Lina", "age": 25},
    "student2": {"name": "Daniel", "age": 34}
}
print(student["student1"])

#--------------Looping through a dictionary--------------
# .keys() -> just the keys
for key in students.keys():
    print(key)
# .values() -> just the values
for value in students.values():
    print(value)
# .items() -> key/value pairs together
for key, value in students.items():
    print(f"{key}: {value}")

"""
 ------------------------------- 
MINI CHALLENGE: STUDENT REPORT CARD
-------------------------------
You need to store and analyze a student's grades.

"""
# 1. Create a dictionary called "report_card" with keys:
#     -"name"
#     - "subject"
#     - "grades" (use a tuple with 3 numbers)
# Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
report_card = {
    "name": "Lina",
    "subject": "Spanish",
    "grades" : (79,78,70)
}
# 2. Print the student's name and subject.
print(report_card["name"])
print(report_card.get("subject"))
# 3. Calculate the average of the 3 grades (HINT: use sum() and len()).
average = sum(report_card.get("grades"))/ 3
print(average)
# 4. Add a new key called "average" with the calculated result.
report_card["average"] = average
print(report_card)
# 5. If the average is 90 or above → print "Excellent!"
#     If between 70 and 89 → print "Good job!"
#     Otherwise → print "Needs improvement!"
if average >= 90:
    print("Excellent!")
elif average >= 70 :
    print("Good job!")
else:
    print("Needs improvement!")
# 6. Remove the "subject" key and print the updated dictionary.
report_card.pop("subject")
print(report_card)