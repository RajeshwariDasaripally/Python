# Program to find the largest number among given numbers
# Asking user to provide input data

a = int(input("Enter the first integer no:"))
b = int(input("Enter the second integer no:"))
c = int(input("Enter the third integer no:"))

# Checking condition and print statement
if(a > b):
    if(a > c):
        print("Suurin:",a)
    else:
        print("Suurin:",c)
elif(b > c):
    print("Suurin:",b)
else:
    print("Suurin:",c)

