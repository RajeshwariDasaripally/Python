"""program to ask user enter integer,until empty input
  writes total number of integers given by the user to a file
use possible exceptions  and check the content of the file"""

filename = "luvut.txt"
# declaring  Total number variable zero
total_numbers = 0
# open file to write
file = open(filename,"w")

# using while loop to iterate till the if condition
while True:
    num = input("Enter as many integers as you want each with enter <exit with double enter> : ")
    file.write(f"{num} ")
    if len(num)==0:     # condition to check user input empty
        break
    else:
        if num.isnumeric():    # condition to check user input numerics
            total_numbers = total_numbers + 1 
        else:
            print("failed to write file" + filename)

file.write(f"\n total_numbers entered: {total_numbers}")       # write file 
# close file
file.close()