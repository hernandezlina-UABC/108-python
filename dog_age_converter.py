# Ask the user to type yhe dog's age in human years
human_years_age = int(input("Enter your dog's age in human years: "))
one_year_dog = 7 # 1 human year === 7 dog years
# We calculate the total dog years by multiplying the user's input by 7
total_dog_years = (human_years_age*one_year_dog)
# print the result
print(f"Your dog is {total_dog_years} years old in dog years")
