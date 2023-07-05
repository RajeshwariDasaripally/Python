# program to show how many ratings(grades) 
# the user gave and average of ratings (grades)
# list declaration for list of ratings
course_grades=[]  
print("Enter grades as many as you want with enter i.e 0 to 5<exit with enter>")
# using while loop to iterate till the if condition
while True:
    num = input("Enter grades: ")   # ask user enter grades 
     
    # condition to check user input empty
    if num == "":
           
        break
    elif int(num) < 0 or int(num) > 5:     # check condition grade shd be 0 t0 5
            print("Invalid input. Grade couldn't be negative or higher than 5")
            continue
    else:
        course_grades.append(int(num))     # add user input grades in list
        length = len(course_grades)        # length of list
        average = sum(course_grades)/length  # calculate average of given grades
# print the length of list
# print average of grades
print(f"Number of grades: {length}")
print (f"Average of grades: {average}")
