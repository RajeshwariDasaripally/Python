# Program to return price of fuel for car trip as a string with 2 decimal place
# d is the amount of kilometers driven,
# c is the average fuel consumption,
# f is the fuel used in litres and p is the price of fuel

def get_cost(d,c,p):
    fuel = d*(c/100)
    get_cost = fuel*p
    format_get_cost = "{:.2f}".format(get_cost)   # .2f is the number of decimals 
    return (f"{format_get_cost} €")

# Function call
print(get_cost(100,7.5,1.88))
print(get_cost(220,6.9,1.88))