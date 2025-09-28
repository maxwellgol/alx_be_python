# finance_calculator.py
# Calculate monthly savings and projected annual savings with simple interest.

# Prompt user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual interest rate
interest_rate = 0.05  # 5%

# Projected savings after one year with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
