# Program to print first letter of users name repeats the length of the name
# Asking user to provide input data

x = str(input("Enter your first name: "))

# Calculating the length of the input string
length = len(x)

# Print the required program
print(f"yourname {x} has {length} letters")
print(length * x[0])
