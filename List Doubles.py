def double_values(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return numbers

def main():
    numbers = [3, 7, 2, 5]
    result = double_values(numbers)
    print(result)

main()