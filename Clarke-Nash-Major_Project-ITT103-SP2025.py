products = {
    1: {"product" : "Butter", "price": 200.00, "stock": 30},
    2: {"product": "Flour (1 lb)", "price": 80.00, "stock": 25},
    3: {"product": "Rice (1 lb)","price": 120.00, "stock": 60},
    4: {"product": "Chicken (1 lb)", "price": 350.00, "stock": 65},
    5: {"product": "Lotion", "price": 150.00, "stock": 100},
    6: {"product": "Juice", "price": 250.00, "stock": 70},
    7: {"product": "Broccoli", "price": 300.00, "stock": 50},
    8: {"product": "Eggs", "price": 600.00, "stock": 15},
    9: {"product": "Toothbrush", "price": 600.00, "stock": 50},
    10:{"product": "Milk", "price": 400.00, "stock": 30},
    11:{"product": "Cereal", "price": 600.00, "stock": 45},
    12:{"product": "Toothpaste", "price": 400.00, "stock": 42}
}
# Empty Cart
myCart = {}

def check_low_stock ():
    for number, details in products.items():
        if details["stock"] < 5:
            print(f"WARNING: {details['product']} has low stock. ({details['stock']} left).")
check_low_stock()

def display_products ():
    print("++++++ Products Catalog ++++++")
    for number, details in products.items():
        print(f"{number}: {details['product']} - ${details['price']} (Stock: {details['stock']})")

def add_item_to_cart ():
    try:
        product_number = int(input("Choose a number to enter a product: "))
        quantity = int(input("Enter the quantity: "))
        if product_number in products:
            product = products[product_number]
            if product["stock"] >= quantity:
                if product["product"] in myCart:
                    myCart[product["product"]] += quantity
                else:
                    myCart[product["product"]] = quantity
                product["stock"] -= quantity
                print(f"{quantity} {product['product']} added to cart.")
            else:
                print("Sorry! Insufficient stock.")
        else:
            print("Invalid product number. Please try again!")
    except ValueError:
        print("Please enter whole numbers only")



def remove_item_from_cart ():
    option = input("Enter 'yes' if you want to clear the entire cart or 'no' to remove a single item: ")
    if option == "yes":
      myCart.clear()
      print("All items have been removed from your cart.")
    elif option == "no":
        item_name = input("Enter the name of the product: ")
        if item_name in myCart:
            if myCart[item_name] > 1:
                myCart[item_name] -=1
                print(f"One {item_name} removed. Remaining: {myCart[item_name]}")
            else:
                del myCart[item_name]
                print(f"{item_name} removed from cart.")
        else:
            print("Item not found in the cart.")
    else:
        print("Invalid input. Please try again")


def view_cart ():
    print("+++++ CURRENT CART +++++")
    for product, qty in myCart.items():
        print(f"{product} - Quantity: {qty}")


def checkout ():
    if not myCart:
        print("Cart is empty. Add items before checkout.")
        return
    #Calucuate totals
    subtotal = sum(products[number]["price"] * qty for number, details in products.items() for product, qty in myCart.items() if details["product"] == product)
    tax = subtotal * 0.1
    total = subtotal + tax
    discount = 0
    discounted_total = total
    if total > 5000:
        discount = total * 0.05
        discounted_total = total - discount
        print("Congratulations! You received a 5% discount!")
    print(f"Subtotal: ${subtotal: .2f}")
    print(f"10% Sales Tax: ${tax: .2f}")
    print(f"Discount: ${discount: .2f}")
    print(f"Total Amount Due: ${discounted_total: .2f}")
    while True:
        try:
            amt_received = float(input("Enter the amount received: "))
            if amt_received >= discounted_total:
                change = amt_received - discounted_total
                print(f"Change: ${change: .2f}")
                print("Thank You for shopping")
                #Generate receipt
                receipt("BEST BUY RETAIL STORE", myCart, subtotal, tax, amt_received, change, discount, discounted_total)
                myCart.clear() #Clear the cart after successful checkout
                break
            else:
                print("Insufficient amount received.")
                print("Options:")
                print("1 - Remove an item from the cart")
                print("2 - Cancel the transaction entirely")
                print("3 - Try another payment amount")

                choice = int(input("Choose an option: "))
                if choice == 1:
                    view_cart()
                    item_to_remove = input("Enter the name of the item to be removed ")
                    if item_to_remove in myCart:
                        qty_to_remove = int(input("Enter the quantity: "))
                        if qty_to_remove >= myCart[item_to_remove]:
                            del myCart[item_to_remove]
                            print(f"{item_to_remove} removed from the cart.")
                        else:
                            myCart[item_to_remove] -= qty_to_remove
                            print(f"{qty_to_remove} {item_to_remove} removed. Remaining: {myCart[item_to_remove]}")
                        #Recalculate total after removal
                        subtotal = sum(products[number]["price"] * qty for number, details in products.items() for product, qty in myCart.items() if details["product"] == product)
                        tax = subtotal * 0.1
                        discounted_total = subtotal + tax
                        print(f"New Total After Removal: ${discounted_total: .2f}")
                    else:
                        print("Item not found in the cart.")
                elif choice == 2:
                    print("Transaction cancelled. Clearing cart......")
                    myCart.clear()
                    break
                elif choice == 3:
                    continue
                else:
                    print("Invalid choice. Please select a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")


def receipt (store_name, cart, subtotal, tax, amt_received, change, discount, discounted_total):
    print("==============================")
    print(f"{store_name.upper()} RECEIPT")
    print("==============================")
    print("Itemized Purchases:")
    for product, qty in cart.items():
        unit_price = next(details["price"] for number, details in products.items() if details["product"] == product)
        total_price = unit_price * qty
        print(f"{product} - Qty: {qty}, Unit Price: ${unit_price}, Total: ${total_price}")
    print("______________________________")
    print(f"Subtotal: ${subtotal: .2f}")
    print(f"10% Sales Tax: ${tax: .2f}")
    print(f"Total Amount Due: ${discounted_total: .2f}")
    print(f"Amount Paid: ${amt_received: .2f}")
    print(f"Change Returned: ${change: .2f}")
    print(f"Discount: ${discount: .2f}")
    print("=============================")
    print("Thank your for shopping with us!")
    print("=============================")

#Main Menu
while True:
    print("==============================")
    print("BEST BUY RETAIL STORE MENU")
    print("==============================")
    print("1 - Display items in stock")
    print("2 - Add an item to cart")
    print("3 - Remove an item from the cart")
    print("4 - View Cart")
    print("5 - Checkout")
    print("6 - Exit")

    try:
        selection = int(input("Choose a number from the menu: "))
        if selection == 1:
            display_products()
        elif selection == 2:
            add_item_to_cart()
        elif selection == 3:
            remove_item_from_cart()
        elif selection == 4:
            view_cart()
        elif selection == 5:
            checkout()
        elif selection == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")






