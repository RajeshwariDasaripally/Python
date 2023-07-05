"""Make a program that tries to write the
 text file 'ayho.txt' (you can decide the content yourself) 
 to the root of the hard drive C of the Windows machine 
 (on macOS/Linux/Unix machines to the user's root directory). 
 What happened? Did the program crash with an error? Fix the program 
so that it does not crash, i.e. add the necessary exception handling."""


filename = "C:/ayho.txt"
# working of try()
try:
    my_file = open(filename,"w")      # open file to write
    my_file.write("This is a test file")
except PermissionError:               # exception handling
    print("Permission denied")
else:                                    # execute if no exception
    print("The content is written in the file")
    my_file.close()
finally:              # this block is always executed  
    print("This is executed")    # regardless of exception generation