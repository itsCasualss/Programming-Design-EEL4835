def range_sum(start, stop):
    total = 0

    for i in range(start, stop + 1):
        total = total + i

    return total

def main():
    start = int(input("Enter starting integer: "))
    stop = int(input("Enter stopping integer: "))

    print("Sum:", range_sum(start, stop))

main()