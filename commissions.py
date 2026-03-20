def calculate_commission(sales_amount):
    return sales_amount * 0.10


sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

commissions = {}

# Calculate commissions
for employee in sales:
    commissions[employee] = calculate_commission(sales[employee])

# Sort by commission (highest first)
sorted_commissions = sorted(commissions.items(), key=lambda x: x[1], reverse=True)

# Print leaderboard
for employee, commission in sorted_commissions:
    print(f"{employee}: ${commission:.2f}")