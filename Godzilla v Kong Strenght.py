def battle(godzilla, kong):

    while godzilla > 0 and kong > 0:

        if godzilla > kong:
            godzilla = godzilla - kong
        else:
            kong = kong - godzilla

    if godzilla > 0:
        return "Godzilla", godzilla
    else:
        return "Kong", kong

def main():
    godzilla = int(input("Godzilla's strength: "))
    kong = int(input("Kong's strength: "))

    winner, strength = battle(godzilla, kong)

    print(winner, "wins!")
    print("Remaining strength:", strength)

main()