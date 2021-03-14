# 3_listTools.py
# A program that calculates the sum, the length, and the average for a given list of numbers.
# Name: Ben Goldstone
# Date: 9/8/2020
listOfNumbers = [10, -5, 14, 0, 47, -12, 17, -4]
total = 0
length = 0
for number in listOfNumbers:
    total += number #adds previous number or initial number to total each time
    length += 1 #adds one each time to count numbers
average = total / length #divides total by length to get average
#prints output
print(f"The List is: {listOfNumbers}")
print()
print(f"Count   = {length}")
print(f"Sum     = {total}")
print(f"Average = {average}")