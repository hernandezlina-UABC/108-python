from catalog import catalog # Import catalog dictionary
# Global variable
cart = []

# Helper Funtion
def header(text):
    print("______________________________________")
    print(text)
    print("______________________________________")
    
def menu():
    print("Menu")
    print(" 1.- View the catalog")    
    print(" 2.- Search Product")    
    print(" 3.- View cart")   
    print(" 4.- Clear cart")   
    # Add more features
    print(" Q.- Quit")
    

#  Catalog and Cart Funtions

def print_catalog():
    header("- Our Catalog -")
    for prod in catalog:         # ljust means left justify. So 15 spaces to the right
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
    
    answer = input("Type ID to add product (N to close): ")
    if answer.lower()== "n": # .lower forces everything to be lowercase
        return
    else:
        add_product_to_cart(answer)


def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id): # matching what user adds to dictionary "id"
            found = True
            cart.append(prod) # add product to the cart
            print(f'{prod["title"]} added to your cart')
            break # Stop after finding and adding product
        
    if not found:
        print("*** ERROR!: Invalid ID ***")
        
def search_prod():
    text = input("Search Title of Product: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
            choice = input("Do you want to add this item to your cart? (y/n)").lower()
            if choice.lower == "y":
                add_product_to_cart(prod["id"])
            break # back to menu
    if not found:
        print("Sorry, this item doesn't exist.")
        
        
def view_cart():
    header("Your Cart")
    if not cart: # Checking if empty firts
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
        cart_total()
"""
1. Create a function calld cart_total():
2. create a variable total
3. loop through the cart items
4. Add the total of all product["price"]
5. print the total
"""
def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
    print(f'${total:.2f} total')


"""
1. Create a function called clear_cart():
2. clear the cart
3. print a message saying "Your cart has been cleared."
"""
def clear_cart():
    cart.clear()
    print("Your cart has been cleared.")
 
    

    
# Main Program Loop
option = ""
while option != "q" and option != "Q":
    header("Welcome to Eco Store")
    menu()

    
    option = input("Choose an option: ")
    
    if option == "1":
        print_catalog()
    elif option == "2":
        search_prod()
    elif option == "3":
        view_cart()
    elif option == "4":
        clear_cart()
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("*** ERROR!: invalid option ***")
    