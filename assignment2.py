print("--------TASKS LIST--------")

# Creating a list of pending tasks
tasks = ["do homework", 
         "create documents for assignments", 
         "eat breakfast", 
         "doctor appoinment",
         "take a 30 min. walk", 
         "videocall familly",
         "pay water bill", 
         "shop vitamins"]
print(tasks)
print(len(agents))

# Accessing items by index
print(f"you need to {(tasks[2])} before you {(tasks[4])}")

# Replacing "pay water bill" for electricity bill
tasks[6] = "pay electricity bill"
print(tasks)

# Removing items (by value or by index)
tasks.pop(1) #removes "create documents for assignments"
print(tasks)

# Printing the list and its length
print (f" YOU HAVE {(len(tasks))} PENDING TASKS.")
for items in tasks:
    print(items)



print("-------VALORANT AGENTS DICTIONARY--------")
# Printing the dictionary and its length after every step
# Add a print after every step
# Creating a dictionary with key:value pairs
# Valorant Agent Dictionary
agents = {
    "name": "Phoenix", 
    "pronouns": "He/Him", 
    "role":"Sentinel", 
    "abilities" : "Fire Blaze, Hot Hands, Fire Curveball"
}
print(agents)
print(len(agents))

# Accessing values using keys
print(agents["name"])

# Adding new keys
agents["ultimate_ability"] = "Run it Back"
print(len(agents))

# Updating existing values
agents["role"] = "Duelist"
print(agents)
print(len(agents))

# Removing keys
agents.pop("pronouns") # removes "pronouns"
print(agents)
print(len(agents))