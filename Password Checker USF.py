password = input("Enter password: ")

if password.startswith("USF") and len(password) >= 8:
    print("Access Granted")
else:
    print("Access Denied")