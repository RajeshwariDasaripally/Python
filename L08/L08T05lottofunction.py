"""Make a function lotto()
draws seven (7) numbers from a lottery row between 1-40 and 
returns it as a string, separated by commas.
 example 1,3,5,10,20,33,39"""

# Python's ready-made module random  
import random
# declaration of list
lottery_num = []

# defining lotto function
def lotto():
    for i in range(7):        # drawing seven number in a lottery row
        # its method to draw numbers randint,between (1-40)     
        num = random.randint(1,40)   
        lottery_num.append(num)    # append num into list
    x = ",".join(map(str,lottery_num))     # returning it as string separated by commas
    print (x)         

# call the lotto function
lotto()

