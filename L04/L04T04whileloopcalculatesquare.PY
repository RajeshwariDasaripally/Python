# Program to show the number and find square of the number 
# Assigning value 1 to a variable (first no.)
i = 1

# Asking user to enter a number
n = int(input("enter number between 1-10:"))

# Using while loop to Iterate till the given number
while i <= n:
    square = i*i
    print(f"Number {i} square:{square}")        # print the statement
    i += 1