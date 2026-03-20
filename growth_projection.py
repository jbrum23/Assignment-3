initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (%): "))

revenue = initial_revenue

print("Year | Revenue")

for year in range(1, 11):
    print(f"{year} | {revenue:.2f}")
    revenue = revenue * (1 + growth_rate / 100)