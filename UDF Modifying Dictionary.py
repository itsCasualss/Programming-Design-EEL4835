def increase_inventory(inventory, amount):
    for item in inventory:
        inventory[item] = inventory[item] + amount

    return inventory

equipment = {
    "Oscilloscope": 5,
    "Multimeter": 8,
    "Function Generator": 3
}

result = increase_inventory(equipment, 2)

print(result)