# Function program that converts temperature
# From celsius to Fahrenheit and vice versa

def celToFah(cel):
    Fah = (float(cel) * 9 / 5 + 32)
    limit_Fah = round(Fah,1)
    return limit_Fah

# Function call
print(celToFah(10.0))

def fahToCel(fah):
    Cel = (float(fah -32) * 5 / 9) 
    limit_Cel = round(Cel,1)
    return limit_Cel

# Function call
print(fahToCel(38.0))