# Program that save data of ten different cars to Dictionary collection
# keys(Registration number) : values (car make)

mycars= {
    "EYK-678":"Skoda",
    "LUB-707":"BMW",
    "EKU-456":"Honda",
    "YKS-834":"Volvo",
    "GYN-097":"Mercedes",
    "AW6-432":"Toyota",
    "YAS-123":"Jaguar",
    "LFI-640":"Suzuki",
    "EUK-346":"Audi",
    "WBH-078":"Tesla"
}

# creates a sorted dictionary (sorted by keys(registration nos))
sortedcars = dict(sorted(mycars.items()))
print(sortedcars)