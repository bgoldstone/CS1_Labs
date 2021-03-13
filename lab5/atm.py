# atm.py
# A program that is a sample atm machine that can print a balance, deposit money, and withdrawal money
# Date: 9/22/2020
# Name: Ben Goldstone
option = "NULL"
balance = 0.00
amount = 0
# Starting Screen
print("Welcome to Kicking Mule Bank")
print("Available Actions")
print("     (B)alance inquiry")
print("     (D)eposit")
print("     (W)ithdrawal")
print("     (Q)uit")
print()

while option != "Q" and option != "q":
    option = input("Please make a selction: ")
    #if user wants to know current balance
    if option == "B" or option =="b":
        print(f"Your current balance is ${balance:.2f}")
    #if user wants to deposit
    elif option == "D" or option =="d":
        amount = float(input("How much money are you depositing? "))
        #verifies amount is not negative
        if amount > 0:
            balance += amount
            print(f"Your current balance is ${balance:,.2f}")
        else:
            print("Invalid amount")
    #ff user wants to withdrawal
    elif option == "W" or option =="w":
        amount = float(input("How much money are you Withdrawing? "))
        #verifies amount is less than or equal to the total balance in the account
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"Your current balance is ${balance:,.2f}")
        else:
            print("Invalid Amount")
    #if user wants to quit ATM, print goodbye message
    elif option == "Q" or option =="q":
        print("Thank You for using Kicking Mule Bank!")
    else:
        print("Invalid Option! Please enter either \"B\", \"D\", \"W\", or \"Q\".")
    print("-"*20)
    print()