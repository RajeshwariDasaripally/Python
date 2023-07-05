# Function program that converts inches into centimeters(cm)
# 1 inch = 2.54 cm
def show_cm(inch):
    cm= (inch * 2.54)
    limit_cm = round(cm,2)
    return (f"{inch} inches is {limit_cm} cm")

# Function call
print(show_cm(2))
print(show_cm(4.5))
print(show_cm(12))

