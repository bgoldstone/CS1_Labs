# 5_pennyBoard.py
# A program that assigns each square on a checkerboard to a set number of pennies getting exponentially bigger
# Date: 9/22/2020
# Name: Ben Goldstone
square  = 1
numberOfPennies = 0.01
#Constants
ONEPENNYTOGRAMS = 2.5
ONEPOUNDTOGRAMS = 453.6
ONEPOUNDOFCOPPERTODOLLARS = 3.15
#counters
totalAmountOfMoney = 0.01
totalWeight = 2.5
print("Square   Number of Pennies")
print("------   -----------------")
for number in range(1,65):
    print(f"{square:}         {int(numberOfPennies*100):,}")
    #adds amount of pennies up
    totalAmountOfMoney += numberOfPennies
    #calculates total weight of pennies
    totalWeight += numberOfPennies * ONEPENNYTOGRAMS
    #adds one to move onto the next square
    square += 1
    #doubles number of pennies
    numberOfPennies *= 2
#converts dollars to pennies and then converts # of pennies to weight in grams
totalWeightInLbs = totalWeight*100/ONEPOUNDTOGRAMS
print(f"Total amount of money on checkerboard ${totalAmountOfMoney:,.2f}")
print(f"Total amount of weight in pennies {totalWeightInLbs:,.2f} lbs")
print(f"Cost of copper to produce pennies ${totalWeightInLbs * ONEPOUNDOFCOPPERTODOLLARS:,.2f}")