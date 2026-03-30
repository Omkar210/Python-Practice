#Budget-Tracker 
month_budget = float(input("Enter your monthly budget: "))
spend = 0
warning = month_budget * 0.8

while True:
    print("1. Add Expense")
    print("2. Add Monthly Budget")
    print("3. View Total Spent")
    print("4. View Remaining Budget")
    print("5. Exit")
    user = int(input("Choose option: "))
    
    if user == 1:
        expense = float(input("Enter your expense: "))
        if month_budget >= expense:
            month_budget -= expense
            spend += expense
            print(f"Expense added. New balance: {month_budget}")
            if spend >= month_budget:
                print("You have reached your budget limit. (100% used)")
            elif spend >= warning:
                print("Warning!! You have reached the 80% of your budget. (80% used)")
        else:
            print(f"You cannot spend more than your budget.  Remaining balance: {month_budget}")
    elif user == 2:
      month_budget += int(input("Add your amount in budget: "))
      print(f"Your amount is added in your total budget. Remaining Balance: {month_budget}")
    elif user == 3:
        print(f"Total spend: {spend}")
        print(f"Remaining Budget: {month_budget}")
    elif user == 4:
        print(f"Remaining Budget: {month_budget}")
    elif user == 5:
        print("Thank you!")
        break
    else:
        print("Please choose a valid option.")