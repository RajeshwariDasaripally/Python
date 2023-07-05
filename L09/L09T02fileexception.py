"""program reads names from the file created 
in previous task displays them on the console. 
program sorts names in alphabetical order and 
displays them on the console in alphabetical order."""

filename = "name.txt"
# open file to read
file = open(filename,"r")
line = file.read()          # read each line
print(line)                 # print names in console

# open file to read and sort lines
file= open(filename)
lines = file.readlines()     # read lines in file
lines.sort()                # sort the lines in file

# Loop through each line of the file
for line in lines:
    # Remove the leading spaces and newline character
    line = line.strip()            
    print(line)               # print the sorted lines in console

# close file
file.close()