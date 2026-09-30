phone = input("Enter phone number: ")

if phone.isdigit() and phone.startswith("1") and len(phone) == 11:
    print("Valid number")
else:
    print("Invalid number")