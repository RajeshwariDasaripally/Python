
# program to write the 10 friend's names in the order
# and also the program to write the friend's names in reverse order
# list declaration
names=[]  
print("Give below the ten friend's names each name with enter")
# using for loop to iterate till the range

for name in range (10):
    name = input("Enter friend name:")  # asking the user input
    names.append(name)   # adding the user input elements in the list
print(names)            # print the list

# reverse the order of list elements
names.reverse()
print("reverse order:",names)  # print the list elements in reverse order
