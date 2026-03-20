customers = {
    "Alice": 800,
    "Bob": 1500,
    "Carol": 5200,
    "Dave": 3000,
    "Eve": 200
}

tiers = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

for customer in customers:
    amount = customers[customer]

    if amount < 1000:
        tiers["Bronze"] += 1
    elif amount < 5000:
        tiers["Silver"] += 1
    else:
        tiers["Gold"] += 1

for tier in tiers:
    print(f"{tier}: {tiers[tier]}")