value = input("Enter something: ")

if value.isalpha():
    print("Only letters")
elif value.isdigit():
    print("Only numbers")
else:
    print("Neither")