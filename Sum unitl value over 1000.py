total = 0
num = 1

while True:
    total = total + num

    if total > 1000:
        break

    num = num + 1

print("Number:", num)
print("Final sum:", total)
