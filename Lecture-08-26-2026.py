#=======================
#A function with arguments
def greet2(name):
    print ("Hello my,", name)
    print (name, ", how may I be of service?")
    
greet2("Austin")

#========================
#another example for a funtion with arguments
def adder (num1,num2):
    print("The sum:", num1+num2)
    
num1=1
num2=9
adder(num1,num2)
adder(1,9)

adder(num2-num1,num1)

#==========================
#Return Values based on UDF
def adder(num1,num2):
    result_sum=num1+num2
    result_difference=num1-num2
    return result_sum, result_difference

num1=1
num2=9

Result1, Result2 = adder(num1,num2)

print("The sum:", Result1)
print("The Difference:", Result2)

#=================================
#Adder UDF and using 'main()' arg
def adder(num1,num2): #defining adder function 
    result_sum=num1+num2 #return sum variable
    result_difference=num1-num2 #return difference variable
    return result_sum, result_difference 

def main():
    num1=6
    num2=7
    Result1, Result2 = adder(num1, num2)
    
    print("The sum:", Result1)
    print("The difference:", Result2)
    
main()


#==============================
#Adder UDF  returning 4 results, based on the 2 num variables .. multiplying, dividing, add/sub
def adder(num1,num2): #defining adder function 
    result_sum=num1+num2 #return sum variable
    result_difference=num1-num2 #return difference variable
    result_multiplication=num1*num2 #Multiply
    result_division=num1/num2 #divide
    return result_sum, result_difference, result_multiplication, result_division 

def main():
    
    num1=1
    num2=9
    Result1, Result2, Result3, Result4 = adder(num1, num2)
    
    print("The sum:", Result1)
    print("The difference:", Result2)
    print("The multiplication:", Result3)
    print("The Division:", Result4)
    
main()

#======================================
#Taking User Input
lbs=input("How Heavy are you?\n")

print("You weigh", lbs, "lbs")
print("You should eat more, Chung Seop.")


#================================
#array, range from 0-3 or 1-4, both outputting 4 instances
for i in range(1,4):
    print("Baka!")
    
print("Would it generate different result?")
    
for i in range (0,3):
    
    print("Baka!")

#=============================
#Becareful! observe the print here is not the sum of the numbers, but a linear combinatoin, 
num1=input("What is the first number?")
num2 = input("What is the second number?")
print(num1+num2)

#===================================
#Temperature converter (F-C and C-F) 

C_Temp=input("Temp in Celcius =>")
C_Temp=eval(C_Temp)
F_Temp=C_Temp*(9/5) + 32
print("It is", F_Temp, "In Fahrenheit!")
#======
F_Temp=input("Temp in Fahrenheit =>")
F_Temp=eval(F_Temp)
C_Temp=(F_Temp -32)*(5/9)
print("It is", round(C_Temp,2), "In Celcius!")

#=================================================
#Data Type and Conversion
num=1
print(type(num),"\n")
num=1.01
print(type(num),"\n")
num1=1.0000000000001 #Since defined as a float, result shows inaccuacy
num2=2.14
print(num1+num2)

#===========================
#TypeCasting
num1=int(input("Type a number:\n"))
num2=float(input("Type another number:\n"))

print("The sum is:", num1+num2)
print("The type of the result is:", type(num1+num2), "\n")
print("If i do type casting,", int(num1+num2))

numd=int(num1+num2)

print("The type of the numd is:", type(numd))
#=====================================
#Simple Loops

for i in [0,1,2]:
    print(i)
    print("Boo~")
print("============")

for i in [0,3,7]:
    print(i)
    print("Boo~")
    
sum=0
for i in [range(0,11)]:
    sum=sum+i
    #sum here is the series sum of 1-10
print("\n",sum)

#==================================






