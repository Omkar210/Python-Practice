
def add_new_product(product, price, quantity):
    product_name = str(input("Enter product name: ")).capitalize()
    if product_name.isalpha() == False:
        return print(f"\nEnter product name correctly.\n")
    elif product_name in product:
        return print(f'\n{product_name} already exists in inventory!\n')
    else:
        product.append(product_name)
        product_price = int(input("Enter price per unit: "))
        if product_price > 0:
            price.append(product_price)
            product_quantity = int(input("Enter quantity: "))
            quantity.append(product_quantity)
        else:
            print("\nPrice cannot be negative or zero.\n")
    return print(f"\n{product_name} added successfully!\n")

def sell_product(product, price, quantity):
    product_name = str(input("Enter product name: ")).capitalize()
    if product_name.isalpha() == False:
        return print(f"\nEnter product name correctly.\n")
    elif product_name not in product:
        print(f"\n{product_name} is not present in the list.\n")
        for i,item in enumerate(product):
            if quantity[i] <= 0:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}")
            elif quantity[i] < 5:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}  ⚠️ LOW STOCK")
            elif quantity[i] >= 5:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}  ✅ Available")
            else:
                print("Error: quantity is not a number.")
    else:
        product_quantity = int(input("Enter quantity to sell: "))
        index = product.index(product_name)
        if product_name not in product:
            print(f"\n❌ {product_name} not found in inventory!\n")
        elif product_name in product and product_quantity > quantity[index]:
            print(f"\n❌ Not enough stock! Only {quantity[index]} units available.\n")
        elif product_name in product and product_quantity <= quantity[index]:
            quantity[index] -= product_quantity
            print(f"✅ Sold {product_quantity} units of {product_name}")
            print(f"💰 Sale Value : ₹{price[index]*product_quantity}")
            print(f"📦 Remaining Stock: {quantity[index]} units")
        else:
            print("\nEnter valid input.\n")

def restock_product(product, quantity):
    product_name = str(input("Enter product name: ")).capitalize()
    if product_name.isalpha() == False:
        return print("\nEnter product name correctly.")

    index = product.index(product_name)

    if product_name in product:
        product_quantity = int(input("Enter product quantity to add: "))
        quantity[index] += product_quantity
        print(f"\n{product_name} restocked! New quantity: {quantity[index]} units\n")
    else:
        print(f"\n{product_name} not found in inventory!\n")

def view_stock_report(product, price, quantity):
    if len(product) > 0:
        sum1 = 0
        print("\n========================================")
        print("            📦 STOCK REPORT             ")
        print("========================================")
        print("No.  Product     Price    Qty     Status")
        print("----------------------------------------\n")
        for i,item in enumerate(product):
            if quantity[i] <= 0:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}  ❌ OUT OF STOCK")
            elif quantity[i] < 5:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}  ⚠️ LOW STOCK")
            elif quantity[i] >= 5:
                print(f"{i+1}.    {product[i]}      {price[i]}     {quantity[i]}  ✅ Available")
            else:
                print("Error: quantity is not a number.")

            print("\n----------------------------------------\n")
        print(f"Total Products: {len(product)}")
        print(f"Total value of inventory: {price[i]*quantity[i]}")
    else:
        print("📭 No products in inventory yet!")
    print("\n========================================\n")

def print_menu():
    print("==============================")
    print("  🏪 SHOP INVENTORY MANAGER  ")
    print("==============================")
    print("1. Add New Product")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. View Stock Report")
    print("5. Exit")
    print("------------------------------\n")

product = []
price = []
quantity = []
while True:
    print_menu()

    check = input("Enter your choice: ")

    if check == '5':
        print("Thank you for using Shop Inventory Manager.")
        break

    if check == '1':
        add_new_product(product, price, quantity)
    elif check == '2':
        sell_product(product, price, quantity)
    elif check == '3':
        restock_product(product, quantity)
    elif check == '4':
        view_stock_report(product, price, quantity)
    else:
        print("Enter the valid option.")