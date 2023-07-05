# Program to find sum of positive integers from given input
# Asking user to provide input data
a = int(input("Enter 1.no:"))
b = int(input("Enter 2.no:"))
c = int(input("Enter 3.no:"))
d = int(input("Enter 4.no:"))
e = int(input("Enter 5.no:"))

# Assign value to sum of numbers 
i = 0

# checking condition and print the statement
if a > 0:
    i += a
if b > 0:
    i += b
if c > 0:
    i += c
if d > 0:
    i += d
if e > 0:
    i += e
    print(f"sum of numbers:{i}")
