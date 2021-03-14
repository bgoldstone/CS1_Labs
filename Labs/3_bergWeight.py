# bergWeight.by
# A program that asks user for the weight of a single Berg Bar and the total number of
# bars made that month as inputs.
# Outputs the total weight of pounds and ounces of all Berg Bar for the month
# Name: Ben Goldstone
# Date 9/8/2020
weightOfSingleBar = float(input("What was the weight of a single Berg Bar? "))
totalNumberOfBars = int(input("How many bars were produced? "))
totalWeight = weightOfSingleBar * totalNumberOfBars #total weight in oz
lbs = int(totalWeight // 16) #Converts oz to lbs
oz = totalWeight % 16 #Takes remainder of oz and keeps them in oz
OZ_TO_GRAMS = 28.34952 #1 oz = 28.34952 grams
barInGrams = weightOfSingleBar*OZ_TO_GRAMS
OZ_TO_KILOGRAMS = 0.02834952 #1 oz = 0.02834952 kilograms
barInKilograms = totalWeight*OZ_TO_KILOGRAMS
#prints output
print("-" * 50)
print(f"Single Berg Bar Weight:       {weightOfSingleBar} oz ({barInGrams:.2f} grams)")
print(f"Total Number of Berg Bars:    {totalNumberOfBars:,} bars")
print(f"Total weight:                 {lbs:,} lbs {oz:.2f} oz ({barInKilograms:.2f} kg)")