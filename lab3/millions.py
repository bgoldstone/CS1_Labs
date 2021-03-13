# millions.py
# Create a list of odd integer number from 1 up to 10,000,000 and finds the total number of numbers,
# the sum of all the numbers, and the average.
# Name: Ben Goldstone
# Date: 9/8/2020
bigList = list(range(0, 10000000, 3))
#print(bigList[0],bigList[1],bigList[2],bigList[3],bigList[-4],bigList[-3],bigList[-2], bigList[-1])
print(f"Minimum Number:          {min(bigList)}")
print(f"Maximum Number:          {max(bigList):,}")
print(f"Sum of all numbers:      {sum(bigList):,}")
print(f"Total number of numbers: {len(bigList):,}")
print(f"Average:                 {sum(bigList)/len(bigList):,.2f}")