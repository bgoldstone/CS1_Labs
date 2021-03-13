# oddEven.py
# A program that asks the user a number for input and tells user if number is even or odd
# Date: 9/22/2020
# Name: Ben Goldstone
num = "0"
while num[0] != "q" and num[0] != "Q":
    num = input("Please enter a number to see if it is even or odd (or enter \"q\" for quit) ")
    # if nothing is typed in prompt user again
    if num == "":
        num = input("Please enter a valid number to see if it is even or odd (or enter \"q\" for quit) ")
    # if user wants to quit the program
    if num[0] == "q" or num[0] == "Q":
        print("Goodbye")
    else:
        # if number is even
        if int(num) % 2 == 0:
            print(f"The number {num} is an even number")
        # else it must be odd
        else:
            print(f"The number {num} is an odd number")
