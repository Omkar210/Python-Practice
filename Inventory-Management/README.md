# Inventory Management System

A simple command-line based inventory management system built in Python. This application allows users to manage shop inventory by adding products, selling items, restocking, and viewing stock reports.

## Features

- **Add New Product**: Add new products to the inventory with name, price, and quantity
- **Sell Product**: Sell products and update inventory quantities automatically
- **Restock Product**: Add more stock to existing products
- **View Stock Report**: Display a comprehensive report of all products with stock status
- **Stock Alerts**: Visual indicators for low stock (⚠️), out of stock (❌), and available (✅) items

## How to Run

1. Ensure you have Python 3.x installed
2. Navigate to the Inventory-Management directory
3. Run the script:

```bash
python inventory_manager.py
```

## Usage

The application presents a menu with the following options:

1. **Add New Product**: Enter product details (name, price, quantity)
2. **Sell Product**: Enter product name and quantity to sell
3. **Restock Product**: Add quantity to existing products
4. **View Stock Report**: See all products with their status
5. **Exit**: Close the application

## Sample Output

```
==============================
  🏪 SHOP INVENTORY MANAGER
==============================
1. Add New Product
2. Sell Product
3. Restock Product
4. View Stock Report
5. Exit
------------------------------

Enter your choice: 4

========================================
            📦 STOCK REPORT
========================================
No.  Product     Price    Qty     Status
----------------------------------------

1.    Apple       50       10      ✅ Available
2.    Banana      20       2       ⚠️ LOW STOCK
3.    Orange      30       0       ❌ OUT OF STOCK

----------------------------------------

Total Products: 3
Total value of inventory: 0
========================================
```

## Requirements

- Python 3.x
- No external libraries required (uses built-in functions)

## Notes

- Product names are case-insensitive and capitalized automatically
- Price must be a positive integer
- Quantity can be zero or positive
- Low stock alert triggers when quantity < 5
- Out of stock when quantity <= 0