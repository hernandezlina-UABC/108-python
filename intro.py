print("Hello world from python!")
print(2)
print(104+300)
print(False)

# SHORT CUT command + s to save

'''
Everything in here
is a comment
'''

name = "Lina"
age = 25
print(name)
print(name, age)

#concatenation
print("My name is: " + name)
print("My name is: " + name + ", and I am " + str(age) +" years old.")

'''
Mini challenge:
1. Create 5 variables
2. Concatenate them into a story
3. Print the story in the terminal
'''

pet_name = "Borer"
pet_owner = "Daniel"
pet_breed = "maltipoo"
pet_age = 11
year = 2021

print("When I met " + pet_owner + " in the year " + str(year)+ "... I looked at his dog " 
      + pet_name + " and afirm him that it was a shitzu but clearly it was a " + pet_breed + 
      " and he just laught... then I asked for the age of his pet too and even though it looked like a puppy it's "
      + str(pet_age) +" years old")

#f-string
print(f"When I met {pet_owner} in the year {year} ... I looked at his dog {pet_name} and afirm him that it was a shitzu but clearly it was a {pet_breed} and he just laught... then I asked for the age of his pet too and even though it looked like a puppy it's {pet_age} years old")

#f-string
place = "disneyland"
activity = "riding the roller coasters"
members = 5
print(f"The last time i went to {place}, Ihad a geart time {activity} with {members} of my friends")

print(f"""This is 
      a multi 
line            {members}
     f-string print statement""")

#Type function
print(type(name))
print(type(age))
print(type(False))

#Casting (changing data types)
print(20 + int("20"))
print(20 + age)

# Input function
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# input to int
new_age = int(input("Enter your age: "))
print(age + new_age)

'''
MINI CHALLENGE:
1. Ask how may slices of pizza and how many people
2. Use math operators to calculate slices per person
3. Show the result using f-string
'''

slices = int(input("how many slices of pizza do you want?: "))
people = int(input("for how many people?: "))
slices_per_person = (slices/people)
print(f"You want {slices} slices of pizza for {people} persons, the slices per person will be {slices_per_person}, do you want to continue with the order?")

