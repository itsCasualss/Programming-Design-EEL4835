def convert_temp(F):
    C = (F - 32) * 5 / 9
    return C

def main():
    F = float(input("Enter temperature in Fahrenheit: "))
    C = convert_temp(F)
    print("Temperature in Celsius:", C)

main()