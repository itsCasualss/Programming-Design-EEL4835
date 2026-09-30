#Godzilla vs Kong - who is taller?

                  

def whom():
    
    godzillaH = input("Please insert Godzilla's Height (in meters)")
    kongH = input("Please insert King Kong's Height (in meters)")
    
    if godzillaH > kongH:
        print("Godzilla is taller than King Kong!")
    elif kongH > godzillaH:
        print("King Kong is taller than Godzilla!")
    else:
        print("King Kong is the SAME height as Godzilla!")
        
whom()

