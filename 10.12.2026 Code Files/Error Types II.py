try:
    num = int(input("Enter a Number:")) #Might Cause ValueError
    result = 10/ (1 - num) #might cause ZeroDivisionError
except ZeroDivisionError:
    print("Cannnot divide by Zero")
except ValueError:
    print("Invalid Input, Please enter a Number!")
else:
    print(f"Success! Result: {result}")

#FileNotFoundError
