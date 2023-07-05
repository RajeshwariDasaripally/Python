"""Make the category Mobile it has three properties: brand ,model, and price.
Add a constructor init to the class, which can be used to set the 
above-mentioned properties when creating an object.
Create two new Mobile objects with the following code:
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)
display the details of both phones on the console."""
# create a class
class Mobile:
    # create constructor init
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    # create str method
    def __str__(self):
        return (f"{self.brand} {self.model} {self.price}")
    
# creating 2 objects with three properties
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)
# object call with properties using str method return
print(phone1)
print(phone2)
