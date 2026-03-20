prices = []

while True:
    price = float(input("Enter item price (0 to finish): "))

    if price == 0:
        break
    elif price < 0:
        print("Invalid input. Price cannot be negative.")
    else:
        prices.append(price)

total_purchase = sum(prices)
number_of_items = len(prices)

if number_of_items > 0:
    average_item_cost = total_purchase / number_of_items
else:
    average_item_cost = 0

print("Total purchase amount:", total_purchase)
print("Average item cost:", average_item_cost)
print("Number of items bought:", number_of_items)