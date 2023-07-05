# Program to separate first name and lastname from character string
# Asking user to provide input data
full_name = (str(input("Enter fullname:")))

# Calculating space position and length of the input
space_position = full_name.find(" ")

# Finding user firstname and lastname positions
f_name = full_name[0:space_position]
l_name = full_name[space_position+1:]


# Printing first name and lastname separately
print("yourfirstname:",f_name)
print("yourlastname:",l_name)