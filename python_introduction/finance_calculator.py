montly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = int(float(montly_income) - float(monthly_expenses))
print(f"Your monthly savings are: ${monthly_savings}.")

projected_savings = int((monthly_savings * 12) + (monthly_savings * 12 * 0.05))
print(f"Your projected savings after one year, with interest, is: ${projected_savings}.")