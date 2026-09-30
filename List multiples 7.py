for i in range(1, 21):
    result = 7 * i

    if result % 2 != 0:
        continue

    print("7 x", i, "=", result)