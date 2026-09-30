def rectangle(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    area, perimeter = rectangle(length, width)

    print("Area:", area)
    print("Perimeter:", perimeter)

main()