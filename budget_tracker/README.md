# Budget Tracker

A simple, interactive command-line application to help you manage your monthly budget and track your expenses effectively.

## Features

- **Set Monthly Budget**: Define your total monthly budget amount
- **Add Expenses**: Track individual expenses and deduct them from your budget
- **Adjust Budget**: Increase your monthly budget at any time
- **View Statistics**: Check total spent and remaining budget balance
- **Smart Warnings**: Automatic alerts when you reach 80% and 100% of your budget limit
- **User-Friendly Interface**: Simple menu-driven navigation for ease of use

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone this repository or download the project files:
```bash
git clone https://github.com/yourusername/budget_tracker.git
cd budget_tracker
```

2. No additional dependencies required - uses only Python's built-in libraries.

### Running the Application

Navigate to the project directory and run:

```bash
python Budget_Tracker.py
```

## Usage

When you run the application, you'll be prompted to enter your monthly budget. Then, you can use the menu to:

1. **Add Expense** - Enter an expense amount to deduct from your budget
2. **Add Monthly Budget** - Increase your total budget
3. **View Total Spent** - See how much you've spent and how much remains
4. **View Remaining Budget** - Check your current available balance
5. **Exit** - Close the application

### Example Session

```
Enter your monthly budget: 1000

1. Add Expense
2. Add Monthly Budget
3. View Total Spent
4. View Remaining Budget
5. Exit
Choose option: 1
Enter your expense: 150
Expense added. New balance: 850

...
```

## Budget Warnings

- **80% Threshold**: You'll receive a warning when total spending reaches 80% of your budget
- **100% Limit**: An alert is shown when you've used 100% of your budget

## Notes

- All amounts are entered as floating-point numbers (e.g., 100.50)
- The application runs in a continuous loop until you choose to exit
- Budget adjustments can be made at any time during the session
- The application will prevent expenses that exceed your remaining budget

## Future Enhancements

Potential features for future versions:
- Expense categories
- Data persistence (save/load budget data)
- Monthly reset functionality
- Expense history and detailed reports
- Graphical user interface (GUI)

## Author

Created as a learning project for Python practice.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

**Happy budgeting!**
