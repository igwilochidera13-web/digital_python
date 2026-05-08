inventory = [
    ["apple", 500, 10],
    ["rice", 1000, 20],
    ["beans", 200, 30],
    ["onions", 100, 15],
    ["pepper", 300, 20]
]

print(inventory[0][2])

for item in inventory:
    price = item[1]

    increased_price = price + (price * .1);

    item[1] = int(increased_price)

# updated_inventory = [item for item in inventory item[1] += int(item[1] * .1)]

print(inventory)
