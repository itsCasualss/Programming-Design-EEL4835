#Intro to Tuples .. Lists = [] whilte Tuples = ().
wh40k_locations = [
    ("Hive City", (-10.7625, 55.8310)),
    ("Macragge's Honour", (0.0000, -0.0012)),
    ("The Fang", (75.3652, 39.7625)),
    ("Terra", (41.9028, 12.4964)),
    ("Krieg", (-77.0369, 38.9072))
]
# Accessing coordinates and city names
for location, coords in wh40k_locations:
    print(f"{location} Coordinates: {coords}")
    #the 'f' [called: f-string] is important after the print function so it recalls the
    #variables from the Tuple, and must be recaled with the {} brackets.



#Important for calling tuple's information 
def your_info(name,age):
    print("Your name is",name)
    print('Your age is',age)
    
your_info('James', 25)
your_info(25, 'James')

print('=================')
your_info(name='James', age=25)
your_info(age=25, name="james")

#in the above, when using the your_info defined function, you must create the referenced arguments - then you can the information without worry.

#the end = ' ' will end the print function with the entered value,
#while sep = ' ' will place the value in between the printed values. 
for i in range(1,6):
    print(i, end="")
    
print(1,2,3,4,sep = "_")

print(1,2,3,4, sep = " ", end = "^^")

def your_info(name, age = 25):
    
#Second argument will have the default value of 0.
#If the user use a value for the second argument, the user value will replace 0.
    print("Your name is", name)
    print("Your age is", age)
    
your_info("Steve")
print("=================")
your_info("Joe", 40)

#You need to default the value in the last entry of the UDF, or else #Error



#
