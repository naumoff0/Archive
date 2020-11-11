import random
import time
import getch
import sys


def scrablator():
    actual = ""
    replacerator = ""
    while True:
        char = getch.getch()

        if char == "\n":  # enter was pressed 
           return float(actual)
        elif ord(char) == 127:  # backspace key was pressed
            if len(actual) > 0:
                # erases previous character.
                sys.stdout.write("\b" + " " + "\b")
                sys.stdout.flush()
                actual = actual[:-1]
        elif char in list("0123456789"):
            sys.stdout.write(scannerator() + "\r")
            sys.stdout.flush()
            actual += char


def scannerator():
    scanstrip = ""
    for i in range(10):
        rando = random.randint(0,3)
        if rando != 0:
            scanstrip += ("#")
        else:
            scanstrip += ("-")
    scanstrip = "|" + scanstrip + "|"
    return scanstrip.rstrip("\n") 


def main():
    while True:
        print("Original Number")
        original = scrablator()
        print("")
        squareBy = int(input("Root by\n>> "))
        print("Calculating...")
        for i in range(100):
            print("{}".format(scannerator()), end = "\r")
            time.sleep(0.01)
        print("|---DONE---|", end = "")
        sqrt = original ** (1 / squareBy)
        print("\n{} is {} to the power of {}".format(original, round(sqrt, squareBy * 3), squareBy))


if __name__ == "__main__":
    main()
        