word = input("Enter a word: ")

amount = 0

for letter in word:
    if letter == "a":
        amount = amount + 1

print("Number of a's:", amount)