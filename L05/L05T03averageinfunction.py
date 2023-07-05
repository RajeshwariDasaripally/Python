# Make a function program to return average of given parameters with one decimal place
def average(a,b,c):
    average = (a+b+c)/3
    format_average = "{:.1f}".format(average)
    return format_average

# Function call
print(average(2,4,6))
print(average(5,5,6))