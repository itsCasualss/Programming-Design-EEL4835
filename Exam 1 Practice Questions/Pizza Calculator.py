#Pizza Calculator
#Ask how many pizzas were ordered
#and how many slices each pizza contains.
#Print the total number of slices.
#Then ask how many people are attending and
#print how many whole slices each person can receive.

ordered = input("How many pizza pies were ordered?\n")
slices = input("How many slices are contained for each pie? \n")

Total_Slices = int(ordered)*int(slices)

print("You have ordered",Total_Slices,"slices of pizza!\n")

attending=input("How many people are attending your pizza party?\n")

per_person = int(Total_Slices) / int(attending)

print("Each person can have at most",per_person,"slices") 
