"""Make the class Cat, it has two properties name and color
 create a method meow. return Meoooooow when it is called
 Create two different cat objects from the Cat class with the following information:
name: Kit, color: black
name: Kat, color: white
Show the properties of the cat objects to the console, also make the cats sleep:"""

# create a class
class Cat:
    name = ""
    color = ""
    # create meow method
    def meow(self):
        return "Meoooooow!"
# creating 2 objects with name and color properties       
cat1 = Cat()
cat1.name = "kit"
cat1.color = "black"

cat2 = Cat()
cat2.name = "kat"
cat2.color = "white"
# object call with properties and method call
print(cat1.name + ", color: "+ cat1.color)
print(cat2.name +", color: "+ cat2.color)
print(cat1.name + " says: " + cat1.meow())
print(cat2.name + " says: " + cat2.meow())


