def add_item(item_name, **item_price):
    total = 0
    item_price = int(item_price[item_name])
    for i in item_price:
        total += item_price[i]
    print("Your provided items are taken considered.")
    return total

def discount():
    if add_item() > 5000:
        discount = add_item()*0.1
    return discount

def cal_total():
    print(f"Total till now is {add_item()*discount()}")
    return add_item()*discount()

def final_bill():
    add = add_item()
    disc = discount()
    print("**********************************")
    print(f"**********Total: {add}************")
    print(f"*********Discount: {disc}*********")
    print(f"***Final Amount: {add+disc}*****")
    print("**********************************")
    return add+disc

items = {}
while True:
    item_input = input("Enter item name and price (or 'done' to finish): ")
    if item_input.lower() == 'done':
        break
    parts = item_input.split()
    if len(parts) == 2:
        items[parts[0]] = int(parts[1])
    else:
        print("Invalid format. Please enter: item_name price")

while True:
    print("**********************************")
    print("**Online-Shopping-Bill-Generator**")
    print("**********************************")
    print("Select any option: ")
    print("**********************************")
    print("1. Add Item")
    print("2. Calculate Total")
    print("3. Print Final Bill")
    print("4. Exit")
    print("**********************************")
  
    check = input("Enter your choise: ")

    if check == '4':
        print()
        print("Thank you for using Online Shopping Bill Generator")
        print("coded by Omkar-Gangamwar")
        break
    if check == '1':
        print(f"Add Item: {add_item(**items)}")
    elif check == '2':
        print(f"Calculate Total: {cal_total(items.values())}")
    elif check == '3':
        print(f"Final Bill: {final_bill(items.values())}")
    else:
        print()
        print("Enter the valid option.")
        print() 
