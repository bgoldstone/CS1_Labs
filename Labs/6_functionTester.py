# 6_functionTester.py
# A program for testing the use of some iterative functions that calculate
# solutions to some simple mathematical problems.
#
# Name: Benjamin Goldstone
# Date: 9/29/2020
#

def main():

    ## DO NOT MODIFY main()
    
    # Get two non-negative integers from the user less than the specified max 
    print("Enter a value for n:")
    num = getIntFromUser(100)
    print()
    print("Enter a value for p:")
    power = getIntFromUser(20)
    # Calculate various interesting things
    summ = summation(num)
    fact = factorial(num)
    expntl = exponential(num, power)
    
    # Provide some nicely formatted output
    printResults(num, power, summ, fact, expntl)

    

# getIntFromUser:
# This function will prompt the user for an integer between 0 and maxNum,
#   and will re-prompt as necessary until a valid input is received.
# Return value: The valid number (integer)
def getIntFromUser(maxNum):
    #### Put a function definition here
    integer = int(input(f"Enter a number between 0 and {maxNum}: "))
    while(integer < 0 or integer > maxNum):
        print("Invalid! Try again.")
        integer = int(input(f"Enter a number between 0 and {maxNum}: "))
    return integer
# Summation:
# Adds up the integers from 1 to n
# Return value: The result (integer)
def summation(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total

# Factorial:
# Calculates the factorial of n
# Return value: The result (integer)
def factorial(n):
        factorial = 1
        for num in range(1, n + 1):
            factorial *= num
        return factorial

# Exponential:
# Takes two integer arguments, n and p.
# Uses a loop to calculate n^p (n raised to the p power)
# Return value: The result (integer)
def exponential(n, p):
   total = 1
   for i in range(p):
       total *= n
   return total

# printResults:
# Prints the input values and results from the program
# Return value: none
def printResults(n, p, s, f, e):
    print("Function tester")
    print("-" * 40)
    print("Inputs:")
    print(f"    n = {n}")
    print(f"    p = {p}")
    print("Results:")
    print(f"    Summation({n})          = {s:,}")
    print(f"    Factorial({n})          = {f:,}")
    print(f"    Exponential: {n}^{p}    = {e:,}")
    print("-" * 40)

# Start the program running
main()   # This must be the last line in the file