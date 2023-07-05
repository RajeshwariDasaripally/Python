# program to Display the entered registration numbers in alphabetical order
# list declaration for list of car registration numbers
car_num=[]  

# using while loop to iterate till the if condition
while True:
    num = input("Enter car reg number:")   # asking the user enter car registration number
    
    if num == "":  # condition to check the user input empty
        break
    else:
        car_num.append(num)    # adding the user input elements in the list

# sorting the list in the alphabetical order (ascending)
car_num.sort()  
# print the sort list
print(car_num)