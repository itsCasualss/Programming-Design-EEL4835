try:
    num = int(input("Enter a Number:")) #Might Cause ValueError
    result = 10/ 0.5*num #might cause ZeroDivisionError
except ValueError:
    result = "Invalid Input, Please enter a Number!"
except ZeroDivisionError:
    result = "Cannnot divide by Zero"

print(result)
#FileNotFoundError