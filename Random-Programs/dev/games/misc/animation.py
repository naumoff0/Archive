import time
from uiHelpers import *
from random import randint

def main():
    rowLength = int(input("Length of rows\n>> "))
    rows = int(input("Number of rows\n>> "))
    printS("Testing output\n", .01)
    for i in range(rows):
        chars = []
        for x in range(rowLength):
            ascii =  chr(randint(1,100000))
            chars.append(ascii)
        printS("".join(chars) + "\n", .01)
if __name__ == "__main__":
    main()