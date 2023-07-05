"""Make the class Human, it has two properties name and age.
Add a str method to the class.
Create two objects of the Human class with the following information: 
Name: Adam, age: 19 and Name: Eva, age: 18"""


# create a class
class Human:
    name = ""
    age = 0
    # create str method
    def __str__(self):
        return (f" name:{self.name}, age:{self.age}")
# creating objects with name and age properties 
h1 = Human()
h1.name = "Adam"
h1.age = 19
h2 = Human()
h2.name = "Eva"
h2.age = 18
# object call 
print(h1)
print(h2)

