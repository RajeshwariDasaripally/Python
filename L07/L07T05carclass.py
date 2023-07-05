"""Make class Car it has three properties:brand, model, and price
Create at least three different car objects from the Car class.
Set the car properties as follows: 1) brand="Skoda" model="Octavia" price=3000 
2) brand="Audi" model="A4" price=4000 3) brand="Volvo" model="V70" price=5000
Print the properties of all three cars in the garage to the console. 
calculate the total price of the cars, and display it on the console:"""

# create a class
class Car:
     # create constructor init
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
# creating 3 objects with three properties    
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)
total_price = car1.price + car2.price + car3.price
# object call with properties and print total cost of cars
print(car1.brand,car1.model,car1.price)
print(car2.brand,car2.model,car2.price)
print(car3.brand,car3.model,car3.price)
print("Cars Total Price:",total_price)

