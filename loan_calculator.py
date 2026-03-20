loan_amount = float(input("Enter loan amount: "))
interest_rate = float(input("Enter annual interest rate (as %): "))
monthly_payment = float(input("Enter monthly payment: "))

balance = loan_amount
months = 0

# convert annual rate to monthly decimal
monthly_rate = (interest_rate / 100) / 12

while balance > 0:
    interest = balance * monthly_rate
    balance += interest
    balance -= monthly_payment
    months += 1

print(f"Loan paid off in {months} months")