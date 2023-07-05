# Program to return consumption of fuel in car trip with 1 decimal place
# d is the amount of kilometers driven,
# c is the average fuel consumption,
# f is the fuel used in litres

def get_fuel(d,c):
    get_fuel = d*(c/100)
    format_get_fuel = "{:.1f}".format(get_fuel)
    return (f"{format_get_fuel} ltr")

# Function call
print(get_fuel(100,7.5))
print(get_fuel(220,6.9))