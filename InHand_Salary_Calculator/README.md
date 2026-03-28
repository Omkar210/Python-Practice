# In-Hand Salary Calculator

A Python application that calculates the **in-hand (net) salary** from gross salary, specifically designed for the **Indian salary structure**. This calculator deducts various mandatory deductions and taxes to provide the actual amount an employee receives.

## Features
- **Gross Salary Input**: Takes user's gross salary as input
- **Standard Deduction**: Applies ₹75,000 standard deduction
- **Provident Fund (PF)**: Calculates 12% of taxable income
- **Professional Tax**: Fixed deduction of ₹2,500
- **Income Tax**: Progressive tax brackets based on Indian income tax slabs:
  - 0% on income up to ₹4,00,000
  - 5% on income ₹4,00,001 to ₹8,00,000
  - 10% on income ₹8,00,001 to ₹12,00,000
  - 15% on income ₹12,00,001 to ₹16,00,000
  - 20% on income ₹16,00,001 to ₹20,00,000
  - 25% on income ₹20,00,001 to ₹24,00,000
  - 30% on income above ₹24,00,000
- **Health & Education Cess**: 4% of income tax
- **Monthly Salary**: Calculates monthly in-hand salary (annual ÷ 12)

## Example Output
```
Enter your gross salary: 1000000
Your new salary is: 813500.0
Your in-hand salary is: 67791.67
```

## Requirements
- Python 3.x