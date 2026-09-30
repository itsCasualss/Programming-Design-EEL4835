# Create UDF ->
    # dog's age in years and additional months as a parameter
        #dog_age(years,months)
    
def dog_age(years,months):
    in_months = years + (months/12)
    return in_months
    
    
    
    
def main():
    years, months = int(input("How many years old is your dog?")) , int(input("How many months old is your dog?"))
    #years,months = 7, 6
    # ===== Replace the comment for lines 13 and 14 if preference is for user input or for predetermined value
    in_months = dog_age(years,months)
    human_years = in_months*7

    
    print("Your dog's equivelant human age is:", human_years,'\n')
    
    if human_years < 14:        
        print("Oh! it must be very cute!")
    elif 14 <= in_months < 35:
        print("Your dog must be quite a handful!")
    elif 35 <= human_years < 70:
        print("Your Dog is in middle age")
    elif 70 <= human_years <91:
        print("Your dog is in its golden age")
    else:
        print("Prepare for a comfortable dog life")
        
        
        
main()
