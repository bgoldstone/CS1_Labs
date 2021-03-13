# lineNumbers.py
# A program that rewrites a file with line numbers
# Date: 10/6/2020
# Name: Ben Goldstone
def main():
    readFileName = input("What is the name of the input file? ")
    writeFileName = input("What do you want the name of your output file to be? ")
    readFile = open(readFileName, "r")
    writeFile = open(writeFileName, "w")
    lineNumber = 1
    for line in readFile:
        writeFile.write(f"{lineNumber:5}." + line)
        lineNumber += 1
    writeFile.close()
    readFile.close()
main()
