# Program to calculate how old the user is
# Asking user to provide input data

fname = str(input("Enter fullname:"))
birth_year = int(input("Enter yearofbirth:"))
from datetime import date
current_year = date.today().year
# Calculating the age of the user
age = current_year-birth_year
# Print the username and age
print(f"Hei {fname},olet {age} vuotta")