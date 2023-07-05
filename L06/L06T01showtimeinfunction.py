# Function program that converts 
# second value in the format hours:minutes:seconds

def showtime(seconds):
    hours = seconds // 3600
    hours1 = seconds % 3600
    minutes = hours1 // 60
    seconds = hours1 % 60 

    return "%02d:%02d:%02d" % (hours, minutes, seconds)

# Function call
print(showtime(500))
print(showtime(10000))
print(showtime(121000))
