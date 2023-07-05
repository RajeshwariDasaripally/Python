"""program that asks for students'names until the user gives an empty input 
 how many names user given and displays them in one line separated by commas."""
 
total_students = 0
students_names = ""

while True:
    names = input("Enter student's name:")
    
    if names == "":
        break
    if students_names == "":
        students_names = names
    else:
        students_names = students_names + "," + names 
    total_students = total_students + 1   
    
print(f"Students: {total_students}")

print(students_names)



