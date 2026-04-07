# Online Shopping Bill Generator

A Python-based command-line application for generating shopping bills with automatic discount calculation. This project demonstrates the use of **kwargs (keyword arguments) in Python functions for flexible item management.

## Overview

This application allows users to:
- Add multiple shopping items with their prices
- Calculate total bill amount
- Apply automatic discounts for purchases over ₹5000
- Generate and display a formatted final bill

## Key Features

- **Interactive Menu System**: User-friendly command-line interface
- **Dynamic Item Addition**: Add items with name and price
- **Automatic Discount**: 10% discount for bills over ₹5000
- **Bill Formatting**: Clean, professional bill display
- **Error Handling**: Input validation and invalid option handling

## Python Concepts Demonstrated

### **kwargs (Keyword Arguments)

**kwargs is a special parameter in Python functions that allows you to pass a variable number of keyword arguments to a function. The arguments are collected into a dictionary.

#### Syntax:
```python
def function_name(required_args, **kwargs):
    # kwargs is a dictionary containing all keyword arguments
    for key, value in kwargs.items():
        # process key-value pairs
```

#### Example in this project:
```python
def add_item(item_name, **item_price):
    # item_price is a dictionary containing item names as keys and prices as values
    total = 0
    for item, price in item_price.items():
        total += price
    return total
```

**Benefits of **kwargs:**
- **Flexibility**: Functions can accept any number of keyword arguments
- **Extensibility**: Easy to add new parameters without changing function signature
- **Dictionary Operations**: Direct access to key-value pairs
- **API Design**: Useful for building flexible APIs and configuration systems

## Usage

1. Run the application:
   ```bash
   python bill_generator.py
   ```

2. Follow the menu options:
   - **Add Item**: Input item name and price
   - **Calculate Total**: View current total with discount
   - **Print Final Bill**: Display formatted bill
   - **Exit**: Close the application

## Example Interaction

```
Enter item name and price (or 'done' to finish): apple 100
Enter item name and price (or 'done' to finish): banana 200
Enter item name and price (or 'done' to finish): done

**********************************
**Online-Shopping-Bill-Generator**
**********************************
Select any option:
**********************************
1. Add Item
2. Calculate Total
3. Print Final Bill
4. Exit
**********************************
Enter your choice: 3

**********************************
**********Total: 300************
*********Discount: 0*********
***Final Amount: 300*****
**********************************
```

## Project Structure

- `bill_generator.py`: Main application file containing all functions and logic

## Learning Outcomes

- Understanding **kwargs for flexible function parameters
- Dictionary manipulation and iteration
- Command-line interface design
- Input validation and error handling
- Modular function design

## Requirements

- Python 3.x
- No external dependencies (uses only built-in Python modules)
