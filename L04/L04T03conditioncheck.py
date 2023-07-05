# Python program to count how many numbers user given, and count the sum of the numbers

# Integers count and total sum variables declaration
sum = 0
count = 0

# Using while loop to iterate until the user gives an empty output
# Condition check: input value is empty or not a digit 

while True:
    number = input("Enter number:")
    if number == "" or number.isdigit() == False:
        break   
    else:
        count += 1
        sum += int(number)
print("numbers given:",count)       # print the statement
print("total sum:",sum)             # print the statement
        
    
 
