'''
A function is a block of code that only runs when its calles.
We can pass data to functiond (parameters), and they can return data as a result.

def fucntion_name(parameters):
    # Code Block (indented)
    # Perform actions using the parameters
    # Return values (optional)
'''

# Simple function without parameters
# It wont run until we CALL the function
def my_function():
    print("This is my function")
# Calling the function
my_function()

# Function with parameters
# Parameters allow us to pass information into a function
def full_name(fname, lname):
    print(f"The name is: {fname} {lname}")

full_name("lina", "hernandez")

# Funtions that return values
# Instead of just printing, function can send back (return) data
def get_full_name(fname, lname):
    return f"{fname} {lname}" # Sends back the full name as text
# Store the returned calue in a variable:
full_name = get_full_name("lina", "hernandez")
print(full_name)

# Functions with default parameters
# A dfefault parameter means the function will use that value
# if no argument is provided when calling the function.
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the class")
    
greet()
greet("lina")

"""
-------------------------------
MINI CHALLENGE: PASSWORD CHECKER
-------------------------------
Create a function called check_password().
1. The function should accept one parameter:
      - password
2. Inside the function:
      - If the password length is 8 or more:
            return "Strong Password"
      - If the password length is between 5 and 7:
            return "Medium Password"
      - Otherwise:
            return "Weak Password"
3. Ask the user to enter a password.
4. Call the function and store the returned result.
5. Print the result.
BONUS:
If the password contains an exclamation mark (!),
print "Special character detected!"
"""

def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    
    elif len(password) >=5:
        return "Medium Password"
    
    else:
        return "Weak Password"

user_password = input("Enter a password: ")
result = check_password(user_password)
print(result)
 

    