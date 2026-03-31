# Business Expense Tracker

A Python function that tracks and categorizes business expenses with a formatted bill summary.

## Function Signature

```python
business_expense(*business_name, expense_name, **expense_amount)
```

## Parameters

### *args - business_name
- **Type**: Variable length positional arguments
- **Description**: Accepts one or more business names
- **Example**: `business_expense("CDAC", "Institute", ...)`
- **Note**: Converts to a tuple of business names

### expense_name (Keyword-only)
- **Type**: Required string argument
- **Description**: The name of the expense category or business identifier
- **Example**: `expense_name="CDAC Institute"`
- **Note**: Must be specified as a keyword argument (comes after *args)

### **kwargs - expense_amount
- **Type**: Variable length keyword arguments
- **Description**: Accepts arbitrary expense items with their amounts
- **Supported Categories**:
  - `staff` → Employee Salary
  - `food` → Food Expense
  - `tea` → Food Expense (grouped with food)
  - `ads` → Advertisement Expense
  - `office` → Office Rent
  - Any other key → Miscellaneous Expense
- **Example**: `staff=50000, food=20000, ads=10000, office=30000, tea=1000`

## Return Value

Returns a formatted string with the total expense amount.

## Usage Example

```python
business_expense(
    "CDAC", 
    expense_name="CDAC Institute", 
    staff=50000, 
    food=20000, 
    ads=10000, 
    office=30000, 
    tea=1000
)
```

**Output**:
```
-----('CDAC',)-----

Bill Summary

--------------------------
Employee Salary: 50000
Food Expense: 20000
Advertisement Expense: 10000
Office Rent: 30000
Food Expense: 1000

Total Expense is: 111000
```

## Features

- **Flexible Input**: Uses *args and **kwargs for flexible expense tracking
- **Expense Categorization**: Automatically categorizes expenses by type
- **Formatted Output**: Displays a well-formatted bill summary
- **Total Calculation**: Automatically calculates and displays total expenses

## Notes

- The function uses positional *args to accept business names
- The `expense_name` argument must be provided as a keyword-only argument
- **kwargs allows for extensible expense categories with dynamic key-value pairs
- Empty expense amounts return an empty dictionary message
- Miscellaneous expenses (unrecognized categories) are included in the total
