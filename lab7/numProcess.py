# numProcess.py
# Counts the number of values, finds the minimum, maximum, average value, and the total of all integers in a file
# Date: 10/6/2020
# Name: Ben Goldstone
def main():
    fileName = input("Please enter an input filename: ")
    readFile = open(fileName, "r")
    writeFile = open("OUT" + fileName, "w")
    firstValue = int(readFile.readline())
    min = firstValue
    max = firstValue
    count = 1
    total = firstValue
    for line in readFile:
        num = int(line)
        if num < min:
            min = num
        if num > max:
            max = num
        count += 1
        total += num
    average = total/count
    writeFile.write("--------------------------------\n")
    writeFile.write(f"Number of values:{count :10,}\n")
    writeFile.write(f"Minimum value:   {min :10,}\n")
    writeFile.write(f"Average value:   {average :13.2f}\n")
    writeFile.write(f"Maximum value:   {max :10,}\n")
    writeFile.write(f"Total:           {total :10,}\n")
    writeFile.write("--------------------------------")
    writeFile.close()
    readFile.close()
main()
