# 4_romanNumerals.py
# A program that converts an Arabic Number to a Roman Numeral between [1-10]
# Date: 9/15/2020
# Name: Ben Goldstone
arabicNumber = int(input("Please enter a number between 1 to 100 to convert to an arabic number: "))
romanNumeralOnes = ""
romanNumeralTens = ""
# Goes through 1-10
if(arabicNumber%10 == 1):
    romanNumeralOnes = "I"
elif(arabicNumber%10 == 2):
    romanNumeralOnes = "II"
elif(arabicNumber%10 == 3):
    romanNumeralOnes = "III"
elif(arabicNumber%10 == 4):
    romanNumeralOnes = "IV"
elif(arabicNumber%10 == 5):
    romanNumeralOnes = "V"
elif(arabicNumber%10 == 6):
    romanNumeralOnes = "VI"
elif(arabicNumber%10 == 7):
    romanNumeralOnes = "VII"
elif(arabicNumber%10 == 8):
    romanNumeralOnes = "VIII"
elif(arabicNumber%10 == 9):
    romanNumeralOnes = "IX"
elif(arabicNumber == 10):
    romanNumeralOnes = "X"
# If bigger than 10 find tens
if(arabicNumber > 10):
    if(arabicNumber < 20):
        romanNumeralTens = "X"
    elif(arabicNumber < 30):
        romanNumeralTens = "XX"
    elif(arabicNumber < 40):
        romanNumeralTens = "XXX"
    elif(arabicNumber < 50):
        romanNumeralTens = "XL"
    elif(arabicNumber < 60):
        romanNumeralTens = "L"
    elif(arabicNumber < 70):
        romanNumeralTens = "LX"
    elif(arabicNumber < 80):
        romanNumeralTens = "LXX"
    elif(arabicNumber < 90):
        romanNumeralTens = "LXXX"
    elif(arabicNumber < 100):
        romanNumeralTens = "XC"
    elif(arabicNumber == 100):
        romanNumeralTens = "C"
    else:
        print("Invalid Number! Please enter numbers between 1 and 100!")
print(f"The Arabic Number {arabicNumber} in Roman Numerals is {romanNumeralTens+romanNumeralOnes}")