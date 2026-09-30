inventory = {
    "Resistor": 25,
    "Capacitor": 12,
    "Inductor": 8,
    "Diode": 20
}

for component, quantity in inventory.items():
    print(component, ":", quantity)