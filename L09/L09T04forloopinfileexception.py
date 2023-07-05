"""program reads the names from the text file(nimet)
tells you how many names are found and 
how many times each name occurs. Using Dictionarycollection """

filename = "nimet.txt"
# open file to read
file = open(filename,"r")

# declaring d as dictionary
d = dict()

# Loop through each line of the file
for line in file:
    # Remove the leading spaces and newline character
    line = line.strip()
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
tot_num_names = len(d)
print (f"Total names:{tot_num_names}")    
# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
# close file
file.close()