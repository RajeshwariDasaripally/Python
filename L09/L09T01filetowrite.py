"""program to enter user with surnames until empty input
  writes names given by the user to a file
possible exceptions when processing the file"""

filename = "name.txt"
# open file to write
file = open(filename,"w")

# using while loop to iterate till the if condition
while True:
    txt_name = input("Enter surname name <exit with enter> : ")
    if len(txt_name)==0:     # condition to check user input empty
        break
    else:
        if txt_name.isalpha():    # condition to check user input alphabeticals
            file.write(f"{txt_name} \n")       # write file    
        else:
            print("failed to write file" + filename)

# close file
file.close()

