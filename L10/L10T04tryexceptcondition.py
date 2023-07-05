"""Make a program where you try 
to change a value in a list that doesn't exist. 
So initialize a list with four elements and then try 
to change the fifth element. Check what kind of exception you get. Fix the 
program so that it does not crash, i.e. add the necessary exception handling."""

# initialize a list with four elements
list = [2,7,9,10]
# working of try()
try:
    list[4] = 5     # try to change the item in list
    print(list)
except IndexError:    # exception handling
    print("sorry, the list assignment index out of range")
finally:              # this block is always executed  
    print("This is executed")    # regardless of exception generation
