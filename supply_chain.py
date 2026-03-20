warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

totals = {}

for warehouse in warehouses:
    inventory = warehouse["inventory"]
    
    for product in inventory:
        if product in totals:
            totals[product] += inventory[product]
        else:
            totals[product] = inventory[product]

for product in totals:
    print(f"{product}: {totals[product]}")