""" create a class Gamecard it has two properties:country and value.
Land is: spade, heart, square or cross.
The value is any number from 2 to 14.
Create five Playing Card entities with different properties.
 display card information as follows print(kortti1.maa , kortti1.arvo)."""

# create a class
class Gamecard:
    land = ""
    value = ""
    
# creating 5 different objects with different properties       
card1 = Gamecard()
card1.land = "spade"
card1.value = 3

card2 = Gamecard()
card2.land = "heart"
card2.value = 6

card3 = Gamecard()
card3.land = "diamond"
card3.value = 8

card4 = Gamecard()
card4.land = "square"
card4.value = 11

card5 = Gamecard()
card5.land = "clubs"
card5.value = 7

# cal the 5 objects with land and value properties
print(card1.land , card1.value)
print(card2.land , card2.value)
print(card3.land , card3.value)
print(card4.land , card4.value)
print(card5.land , card5.value)


