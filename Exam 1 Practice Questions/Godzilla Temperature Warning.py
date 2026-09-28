#Godzilla Temperature Warning
C_Temp=input("Advise the Temperature Reading in Celcius: ")
C_Temp=eval(C_Temp)

def Godzilla_Temp():
    F_Temp=C_Temp*(9/5) + 32
    print('It is', F_Temp, 'In Fahrenheit')
    if F_Temp >= 100:
        print("Godzilla Weather!")
        
        
        
Godzilla_Temp()
