"""program to ask the user age 
   program function kerro3() 
   conditions to check if the age is less than 13 years, "child" is 
returned * if the age is 13-19 years, "teen" is returned * 
if it is 20-65 years, "adult" is returned * otherwise "senior"."""
# asking user to enter age
age = int(input("Enter your age:"))
# creating kerro3 function
def kerro3(): 
    # three conditions to check age and return according to the age  
    if age < 13:
        print("child")
    elif age >= 13 and age <= 19:
        print("teen")
    elif age >= 20 and age <= 65:
        print("adult")
    else:
        print("senior")
# cal the function kerro3
kerro3()