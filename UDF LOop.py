def count_above(numbers, limit):
    count = 0

    for num in numbers:
        if num > limit:
            count = count + 1

    return count

data = [12, 5, 18, 7, 21, 3, 16]

result = count_above(data, 10)

print(result)