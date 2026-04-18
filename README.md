# Python Practice Repository

A comprehensive collection of Python practice projects showcasing various programming concepts and real-world applications. This repository is actively maintained with new projects and improvements added regularly.

## Overview

This repository demonstrates practical Python skills including:
- Control flow (if-else, loops)
- Functions and modular programming
- Data structures (lists, dictionaries, tuples, sets)
- Object-oriented programming (OOPS)
- Exception handling
- Real-world problem solving

## Projects

### 1. **In-Hand Salary Calculator**
`InHand_Salary_Calculator`

A Python application that calculates **net (in-hand) salary** from gross salary according to the **Indian salary structure**. This calculator applies all mandatory deductions and taxes to compute the actual amount an employee receives monthly.

**Key Features:**
- Gross salary input validation
- Standard deduction: ₹75,000
- Provident Fund (PF): 12% deduction
- Progressive income tax brackets
- Health & Education Cess: 4%
- Monthly salary calculation

**Technology:** Pure Python  
**Difficulty Level:** Beginner to Intermediate

[View Project Details →](./InHand_Salary_Calculator/README.md)

---

### 2. **Secret Number Guessing Game**
`Secret_Number`

An interactive command-line game where one player sets a secret number and another player tries to guess it within a limited number of attempts. Features secure input handling and clear game feedback.

**Key Features:**
- Secure number input using `getpass` module
- Limited attempts (5 tries max)
- Real-time feedback on guesses
- Lives tracking system
- Game-over detection

**Technology:** Python (with `getpass` module)  
**Difficulty Level:** Beginner

[View Project Details →](./Secret_Number/README.md)

---

### 3. **Inventory Management System**
`Inventory-Management`

A command-line inventory management system for managing shop stock. This application allows users to add products, sell items, restock inventory, and generate stock reports with visual status indicators.

**Key Features:**
- Add new products with price and quantity
- Sell products and update stock automatically
- Restock existing products
- View comprehensive stock reports
- Stock status alerts (available, low stock, out of stock)
- Simple menu-driven interface

**Technology:** Pure Python  
**Difficulty Level:** Beginner to Intermediate

[View Project Details →](./Inventory-Management/README.md)

---

### 4. **Budget Tracker**
`budget_tracker`

A simple, interactive command-line application to help you manage your monthly budget and track your expenses effectively. This tool provides budget monitoring with automatic alerts and expense tracking capabilities.

**Key Features:**
- Set and adjust monthly budget
- Add individual expenses with automatic deduction
- View total spent and remaining balance
- Smart budget warnings at 80% and 100% usage
- User-friendly menu-driven interface
- Real-time budget status updates

**Technology:** Pure Python  
**Difficulty Level:** Beginner

[View Project Details →](./budget_tracker/README.md)

---

### 5. **Business Expense Tracker**
`track_business_expense`

A Python function designed to track and categorize business expenses with automatic bill summary generation. This utility handles multiple business entities and expense types using flexible argument handling.

**Key Features:**
- Track expenses for multiple businesses
- Automatic expense categorization (staff, food, ads, office, etc.)
- Formatted bill summary output
- Support for variable business names and expense types
- Calculation of total expenses
- Grouped expense reporting

**Technology:** Pure Python  
**Difficulty Level:** Intermediate

[View Project Details →](./track_business_expense/README.md)

---

### 6. **Online Shopping Bill Generator**
`online_shoping_bill_generator`

A Python-based command-line application for generating shopping bills with automatic discount calculation. This project demonstrates the practical use of **kwargs (keyword arguments) in Python functions for flexible item management and bill processing.

**Key Features:**
- Interactive menu system for bill management
- Dynamic item addition with name and price
- Automatic 10% discount for bills over ₹5000
- Formatted final bill display
- Input validation and error handling
- **kwargs implementation for flexible function parameters

**Technology:** Pure Python  
**Difficulty Level:** Intermediate

[View Project Details →](./online_shoping_bill_generator/README.md)

---

### 7. **To-Do List Manager**
`To-Do_list_Manager`

A simple command-line diary and to-do list manager that saves encrypted notes to a file. This project demonstrates file I/O, password-protected access, and XOR-based text encryption.

**Key Features:**
- Password-protected diary access
- Encrypted file storage using XOR encoding
- Write diary entries and read decrypted content
- Menu-driven interface for user actions
- File error handling for missing diary files

**Technology:** Pure Python  
**Difficulty Level:** Intermediate

[View Project Details →](./To-Do_list_Manager/README.md)

---

### 8. **My Diary**
`My_Diary`

A password-protected diary application that stores encrypted notes and lets users write/read entries from the command line.

**Key Features:**
- Password-protected diary access
- XOR-based encryption for stored notes
- Write and read diary entries
- Simple menu-driven interface

**Technology:** Pure Python  
**Difficulty Level:** Beginner to Intermediate

[View Project Details →](./My_Diary/README.md)

---

## Getting Started

### Prerequisites
- Python 3.x installed
- Basic understanding of command-line usage

### Running a Project

Navigate to any project directory and run:

```bash
python filename.py
```

**Example:**
```bash
cd InHand_Salary_Calculator
python inhand_salary.py
```

---

## Repository Structure

```
Python-Practice/
│
├── README.md (This file)
│
├── budget_tracker/
│   ├── Budget_Tracker.py
│   └── README.md
│
├── InHand_Salary_Calculator/
│   ├── inhand_salary.py
│   └── README.md
│
├── Inventory-Management/
│   ├── inventory_manager.py
│   └── README.md
│
├── online_shoping_bill_generator/
│   ├── bill_generator.py
│   └── README.md
│
├── To-Do_list_Manager/
│   ├── to-do_list.py
│   └── README.md
│
├── My_Diary/
│   ├── my_diary.py
│   └── README.md
│
├── Secret_Number/
│   ├── secret_number_game.py
│   └── README.md
│
└── track_business_expense/
    ├── track_business_expense.py
    └── README.md
```

---

## Development Status

**Active Development** - New projects and features added regularly

### Current Activity
- Daily updates and improvements
- New projects added frequently
- Code refinement and optimization
- Enhanced documentation

---

## Future Roadmap

### Phase 1: Core Projects Expansion (In Progress)
- [x] InHand Salary Calculator
- [x] Secret Number
- [x] Budget Tracker Application
- [x] Track Business Expense
- [x] Inventory Management
- [x] Online Shopping Bill Generator
- [x] Todo List Manager
- [x] My_Diary (Mini-Project)

### Phase 2: Intermediate Projects
- [ ] File handling projects (CSV/JSON processing)
- [ ] Web scraping utilities
- [ ] Database interaction scripts
- [ ] Email automation tools

### Phase 3: Advanced Projects
- [ ] Object-oriented design patterns
- [ ] REST API development (Flask/FastAPI)
- [ ] Data analysis with Pandas
- [ ] Automation scripts

### Enhancements
- [ ] Unit testing for all projects
- [ ] Input validation improvements
- [ ] Error handling refinements
- [ ] GUI versions of applications
- [ ] Performance optimizations

---

## Learning Path

Recommended order for learners:

1. **Secret_Number** - Learn basic loops, conditionals, and game logic
2. **InHand_Salary_Calculator** - Practice nested conditionals and calculations
3. **Upcoming Projects** - Progressively advanced concepts

---

## Project Details

Each project folder contains:
- **`<project_name>.py`** - Main Python script
- **`README.md`** - Detailed project documentation with:
  - Feature descriptions
  - Usage examples
  - Future improvements
  - Requirements

---

## Technology Stack

- **Language:** Python 3.x
- **Modules Used:**
  - `getpass` - Secure password/number input
  - `collections` - Advanced data structures
  - `math` - Mathematical operations
  
Future projects will include frameworks like Flask, FastAPI, Pandas, and more.

---

## Code Standards

All projects follow these practices:
- Clear variable naming conventions
- Proper function documentation
- Comments for complex logic
- Modular code structure
- Input validation

---

## Goals

- Build a strong foundation in Python programming
- Create practical, real-world applications
- Master various programming concepts
- Develop problem-solving skills
- Maintain clean, readable code

---

## Notes

- Projects are beginner-friendly and well-commented
- Each project is independent and can run standalone
- No external dependencies required (unless specified in project README)
- Perfect for learning and portfolio building

---

## Learning Resources Used

- Official Python Documentation
- Programming concepts and algorithms
- Real-world problem scenarios
- Best practices in software development

---

## Update Frequency

**Daily Updates** - This repository is actively maintained with:
- New projects added regularly
- Bug fixes and improvements
- Enhanced documentation
- Code optimizations

Last Updated: **March 2026**

---

## Quick Links

- [In-Hand Salary Calculator →](./InHand_Salary_Calculator/)
- [Secret Number Game →](./Secret_Number/)
- [Budget Tracker →](./budget_tracker/)
- [Track Business Expense →](./track_business_expense/)
- [Inventory Management →](./Inventory-Management/)
- [Online Shoping Bill Generator ->](./online_shoping_bill_generator/)
- [To-Do List Manager ->](./To-do_list_manager/)
- [My_Diary ->](./My_Diary/)

---

## Future Contributions

Stay tuned for:
- More intermediate projects
- Advanced programming concepts
- Real-world applications
- Complete project deployments

---

**Happy Coding!**

*This repository showcases Python learning journey with practical implementations and continuous improvement.*
