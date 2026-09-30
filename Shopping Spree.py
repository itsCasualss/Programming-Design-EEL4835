money = 1000
items = 0

while money > 0:
    price = float(input("Item price: "))
    money = money - price
    items = items + 1
    print('Money Left:', money)

print("Items purchased:", items)