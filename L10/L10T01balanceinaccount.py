"""1.Introduce a variable saldo  and mention the intial amount €2000
   2.Print the bank account balance to the console.
   3.user input in the console for euros and cents separatly
   4.Print the latest balance amount in the saldo account"""
#Initialise the saldo named variable with the bank account 
saldo = 2000 
# balance account in euros in bank
print(f"Bank account balance: {saldo} €")
# user input total amount of euros and cents
euros = int(input("Enter the amount of euros:"))
cents = int(input("Enter the amount of cents:"))
# calculating the total user entered amount and adding into saldo named account
total_money = euros + (cents/100)
saldo = saldo + total_money
# printing the total final balance in the saldo account
print(f"Bank account balance: {saldo} €")



