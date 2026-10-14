#Raising Custom Errors

def check_age(age):
    if age < 0:
        raise ValueError("Age Cannon be negative!")
    return f"Valid Age:{age}"


try:
    print(check_age(-5))
except ValueError as e:
    print(f"Error:{e}")