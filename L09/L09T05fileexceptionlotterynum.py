"""program that draws lottery lines 
saves them in the text file 'lotto.txt'
The drawn row contains seven (7) numbers between 1-40. 
The user is asked how many lines will be drawn.  
make sure that the same number does not appear twice in a row."""

import random

#Initialise an empty list that will be used to store the 7 lottory numbers!
#asking user to iput number of lines to draw
l = int(input("Enter How many lines to be drawn: "))
# open the file lotto.txt file to write
with open ("lotto.txt", "w") as file:
    # using for loop to iterate till the range (user given no of lines)
    for line in range(l):
        #Initialise an empty list that will be used to store lottory numbers!
        lotteryNumbers = []
        # for loop iterate till the range to collect 7 numbers in a line
        for i in range (7):
            # To draw random number between 1 and 40
            number = random.randint(1,40)
            #Check if this number has already been picked or not
            while number in lotteryNumbers:
                # if it has, pick a new number instead 
                number = random.randint(1,40)
            #Now that we have a unique number, let's append it to our list.
            lotteryNumbers.append(number)
            # write the number in file
            file.write(str(number))
            if i != 6:
                file.write(", ") 
        file.write("\n")       # write in the new line for the next iteration
