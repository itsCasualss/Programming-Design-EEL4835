from random import randint

num = randint(1, 100)

print("Generated number:", num)

if num % 7 == 0:
    print("Lucky!")
else:
    print("Try again!")
    
