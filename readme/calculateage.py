#Program to print current date and calculate the age of the user.
#Asking user to provide input name and year of birth
#import a datetime library to access current year
import datetime
#asking user input in console
full_name = str(input("Enter fullname:"))
birth_year = int(input("Enter year of birth:"))
#declaring a variable current_date and set date into it
current_date = datetime.datetime.now()
#declaring a variable current_year and set the current year
current_year = current_date.year

#Calculating the age of the user
age = current_year-birth_year

#Print the  current date and username with age
print("Todays date and time: ",current_date) 
print(f"Hello {full_name},you are {age} years")