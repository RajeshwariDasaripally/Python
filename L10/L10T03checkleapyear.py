"""program to check input year is leap year or not 
   asking user to enter year  
   A Leap Year must be divisible by four. 
   But Leap Years donot happen every four years … there is an exception.
If the year is also divisible by 100, it is not a Leap 
Year unless it is also divisible by 400.  
check for these E.g. 1991 -> no, 1992 -> on, 1900 -> no, 2000 -> on"""

# asking user input to check the year leap or not
input_year = int(input("Enter the Year : "))
# checking if condition 
if (( input_year%400 == 0)or (( input_year%4 == 0 ) and ( input_year%100 != 0))):
    print(f"{input_year} is Leap Year!")
else:
    print(f"{input_year} is  not a Leap Year!")
