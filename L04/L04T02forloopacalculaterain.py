# Program to calculate and display the total amount of rain for the week

# Assign value to variables
number_of_days = 7
total = 0

# Using for loop to iterate till the end
for i in range(number_of_days):
    rainfall = int(input("Enter rainfall:"))
    total += rainfall

print("Rainfall total:",total)        # print the statement