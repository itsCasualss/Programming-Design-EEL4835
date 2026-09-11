#print number of chars found in string 
str = ["United States of America", "Korea", "Japan", "China"]
count = 0
for cha in str:
    print(cha)
    for spe in cha:
        if spe == "a":
            count += 1
print(count)
#Print result if & Only if answer is even 
for num in range (2,101):
    if num%2 ==0 or num %3 ==0:
        continue
    print(num)
    
for num in range (1,10):
    if num*7 %2 !=0:
        continue
    print("7 x", num, "=", 7*num)
  
#For and While, Finding the LCM and GCD 
def main():
    i=1
    
    while True:
        if i % 6==0 and i % 45 ==0:
            print("The Lease common multiple b/w 6 and 45 is",i,end="")
            break
        i= i+1
main()


def main():
    i=42
    
    while True:
        if 42 % i == 0 and 120 % i ==0:
            print ('The greatest common divisor between 42 and 120 is', i, end='')
            break
        i=i-1
#Series sum for i until desired value (100 or more here)
def main():
    i=1
    sum=0
    while True:
        sum=sum+i
        if sum>100:
            print('With the current value of i being',i,'the sum is',sum,end='')
            break
        i=i+1
main()

#Break Function introduction
def main():
    i=1
    while i < 100:
        
        print(i,end = " ")
        i = i+1
        if i==20: break
    print("\n")
    print(i)
main()
#while function, continuously trys increasing i values until 63 is reached. 
def main():
    i=1
    while 3*i/2 !=63:
        i=i+1
    print(i)
    
main()

#While Loops
def main():
    sum = 0
    i = 0
    while i <= 10:
        sum=sum+i
        i += 1
    print("sum = ", sum, end = ' ')

main()

#If you know the exact # of iterations, use for,
#if the exact number is unknown, use while


#Sum 
def main():
    i=1
    sum = 0
    while True:
        sum = sum +i
        if sum >100:
            print("With the current value of i being", i, "the sum is", sum, end = " ")
            break
    i = i+1
main()







main()
