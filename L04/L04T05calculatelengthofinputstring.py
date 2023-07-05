# Program to print 
# 1.first letter of users name repeats the length of the first name 
# 2.users last name in reverse order

# Asking user to provide input data
x = str(input("enter your firstname: "))
y = str(input("enter your lastname: "))

# Calculating the length of the input string
length = len(x)

# Print the given statement
print(length*x[0],y[::-1])