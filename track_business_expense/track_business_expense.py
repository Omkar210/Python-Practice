def business_expense(*business_name, expense_name, **expense_amount):
    """Input: Business name, expense name, expense amount"""
    total_expense = 0
    print(f"-----{business_name}-----")
    print()
    print("Bill Summary")
    print()
    print("--------------------------")
    if len(expense_amount) == 0:
        return f"{business_name} Expense is: {expense_amount}"
        
    for i in expense_amount:
        if i == "staff":
            print(f"Employee Salary: {expense_amount[i]}")
            total_expense += expense_amount[i]
        elif i == "food" or i == "tea":
            print(f"Food Expense: {expense_amount[i]}")
            total_expense += expense_amount[i]
        elif i == "ads":
            print(f"Advertizement Expense: {expense_amount[i]}")
            total_expense += expense_amount[i]
        elif i == "office":
            print(f"Office Rent: {expense_amount[i]}")
            total_expense += expense_amount[i]
        else:
            print(f"Miscellanious Expense: {expense_amount[i]}")
    
    return f"\nTotal Expense is: {total_expense}"

print(business_expense("CDAC", expense_name="CDAC Institute", staff=50000, food=20000, ads=10000, office=30000, tea=1000))