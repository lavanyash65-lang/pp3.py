# Simple Interest Calculation

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (% per annum): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: {simple_interest:.2f}")

# Compound Interest Calculation

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (% per annum): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter number of times interest applied per year: "))

amount = principal * (1 + rate/(100*n))(n*time)
compound_interest = amount - principal

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {amount:.2f}")
