import linecache
import termcolor
import hashlib
import termios
import random
import getch
import file
import time
import sys
import os


def printS(text, delay = .02, color=None):
    enableEcho(False)
    for char in text:
        if color is not None:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()
        time.sleep(delay)

    enableEcho(True)

    # flush input
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    

def verifyInput(acceptedInput):
    printS("\n>> ", .02)
    choice = input()
    choice = choice.lower()

    # convert all accepted input to lowercase (disable if need be)
    acceptedInput = [x.lower() for x in acceptedInput]
    firstRun = True

    while choice not in acceptedInput:
        if firstRun:
            replaceLines(1)
            firstRun = False
        else:
            replaceLines(3)

        printS("\nInput invalid!\n", "red")

        printS(">> ", .02)
        choice = input()
        choice = choice.lower()

    return choice


def prompt(message, functionToRun=None):
    printS(message + " [y/n]:", .02)
    choice = verifyInput(["y", "n"])

    if functionToRun is not None and choice == "y":
        functionToRun()
        return

    return choice


def cls():
    os.system("clear")


def replaceLines(linesToDelete):
    cursorOneUp = "\x1b[1A"
    eraseLine = "\x1b[2K"

    for _ in range(linesToDelete):
        sys.stdout.write(cursorOneUp)
        sys.stdout.write(eraseLine)


# from https://gist.github.com/kgriffs/5726314
def enableEcho(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)


class menu:
    def __init__(self, header, subHeader=None):
        self.header = header
        self.subHeader = subHeader
        self.menuItems = dict()

    def display(self):
        while True:
            cls()

            # print menu header and subHeader if specified
            printS(self.header + "\n")

            if (self.subHeader is not None):
                printS(self.subHeader)

            # print line seprator for title
            for _ in range(len(self.header) + 5):
                print("─", end="")

            print()

            for itemNumber, description in sorted(self.menuItems.items()):
                printS("{}) {}\n".format(itemNumber, description[0]))

            print()

            choice = None
            firstRun = True
            while True:
                choice = self.menuItems.get(input(">> "))

                if choice is not None:
                    break

                if not firstRun:
                    replaceLines(1)

                replaceLines(1)
                printS("Invalid Option!\n", "red")
                firstRun = False

            # function adress
            functionToRun = choice[1]
            args = choice[2]
            
            # unpack args to function if provided
            if args != "()": functionToRun(*args)
            else: functionToRun()
                
            self.exit()

        return

    def addItem(self, description, route, inDev=None, *args):
        if inDev:
            spacesToPrint = 20 - len(description)
            for _ in range(spacesToPrint):
                description = description + " "
                
            description = description + "(dev)"
        elif inDev == False:
            return
        
        
        itemNumber = len(self.menuItems) + 1
        self.menuItems.update({str(itemNumber): [str(description), route, args]})

        return

    def load(self, description, debug):
        if debug:
            return
        
        cls()
        with open("game/content/logo.txt", "r") as logo:
            for line in logo:
                print(line, end="")

        files = file.findFiles(".py")
        print()

        try:
            for n in range(len(files)):
                enableEcho(False)
                filePath = files[n].lstrip(os.getcwd())
                progress = round(((n + 1) / len(files)) * 100)

                print(description + " [{}]".format(filePath))
                print("[{}%] Complete".format(progress))

                randomTime = random.randint(3, 8)
                time.sleep(randomTime / 100)
                replaceLines(2)
                

            enableEcho(True)
        except (KeyboardInterrupt, SystemExit):
            raise

    def exit(self):
        if prompt("\nReturn back to menu?") == "n":
            raise SystemExit


def twoOption(optionOne, optionOneSelect, optionOneFunc, optionTwo, optionTwoSelect, optionTwoFunc):
    printS("\r{}({})< >{}({})    \r{}({})<".format(optionOne, optionOneSelect, optionTwo, optionTwoSelect, optionOne, optionOneSelect))
            
    while True:
        char = getch.getch()
        if char.lower() == optionOneSelect.lower():
            print()
            cls()
            return char.lower()
            
        elif char.lower() == optionTwoSelect.lower():
            print()
            cls()
            return char.lower()
            
        else:
            if char != "\n":
                printS("inputErr>{}({})".format(optionTwo, optionTwoSelect))
                
            elif char == "\n":
                printS("enter>{}({})".format(optionTwo, optionTwoSelect))
            
            printS("\r{}({})< >{}({})         \r{}({})<".format(optionOne, optionOneSelect, optionTwo, optionTwoSelect, optionOne, optionOneSelect))
            