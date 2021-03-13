# factorial.py
# A program that asks the user for input and tells user what that numbers factorial is
# Date: 9/22/2020
# Name: Ben Goldstone
num = 0
while num >= 0:
    num = int(input("Enter an integer (negative to quit): "))
    factorial = 1
    # if negative print a goodbye message
    if num < 0:
        print("Done!")
    else:
        for number in range(1, num + 1):
            factorial *= number
        print(f"{num}! = {factorial}")
