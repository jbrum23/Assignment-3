import random

portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0
for stock in portfolio:
    total_value += portfolio[stock]["shares"] * portfolio[stock]["price"]

print("Initial total portfolio value:", total_value)

for day in range(1, 6):
    total_value = 0

    for stock in portfolio:
        # simple random change: -5%, 0%, or +5%
        change = random.choice([-0.05, 0, 0.05])
        portfolio[stock]["price"] = portfolio[stock]["price"] * (1 + change)

        total_value += portfolio[stock]["shares"] * portfolio[stock]["price"]

    print(f"Day {day} total portfolio value: {total_value:.2f}")