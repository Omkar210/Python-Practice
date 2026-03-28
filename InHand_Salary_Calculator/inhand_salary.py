# Calculate the In-Hand Salary from Gross salary
gross = float(input("Enter your gross salary: "))
std_deduction = 75000
tax_amount = gross - std_deduction
pf = tax_amount* 0.12
prof_tax = 2500
income_tax = 0

if tax_amount<= 4000000:
    income_tax = 0
elif tax_amount<= 800000:
    income_tax = tax_amount* 0.05
elif tax_amount <= 1200000:
    income_tax = tax_amount *0.1
elif tax_amount <= 1600000:
    income_tax = tax_amount * 0.15
elif tax_amount <= 2000000:
    income_tax = tax_amount * 0.2
elif tax_amount <= 2400000:
    income_tax = tax_amount * 0.25
else:
    income_tax = tax_amount * 0.3
health_education_cess = income_tax * 0.04

new_salary = gross - pf - std_deduction - prof_tax - income_tax - health_education_cess
print(f"Your new salary is: {new_salary}")
print(f"Your in-hand salary is: {new_salary/12}")
