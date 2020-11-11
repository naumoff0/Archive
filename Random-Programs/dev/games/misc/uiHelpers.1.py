from collections import OrderedDict
from termcolor import colored
import progressbar
import linecache
import hashlib
import termios
import getch
import time
import sys
import os


menuItems = dict()


def bar(length, delay):
    bar = progressbar.ProgressBar()
    for i in bar(range(length)):
        time.sleep(delay)


def printS(text, delay, color=None):
    # print with delay function
    enableEcho(False)
    for char in text:
        if color is not None:
            sys.stdout.write(colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()
        time.sleep(delay)

    enableEcho(True)

    flushInput()


def verifyInput(acceptedInput):
    # flushInput()

    printS("\n>> ", 0.03)
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
            replaceLines(4)

        printS("\nInput [{}] INVALID\n".format(choice), 0.015, "red")
        printS("Accepted Input >> {}\n".format(acceptedInput), 0.015, "green")

        printS(">> ", 0.03)
        choice = input()
        choice = choice.lower()

    return choice


def makeMenu(header, subHeader=None):
    cls()

    # print menu header and subheader if specified
    printS(header + "\n", 0.015)

    if (subHeader is not None):
        printS(subHeader, 0.015)

    # print line seprator for title
    for i in range(len(header) + 5):
        print("─", end="")

    print("")
    global menuItems

    # sort menu items by key so lowest is at top and then display them
    for itemNumber, description in sorted(menuItems.items()):
        # description is a mini list (description, route)
        printS("{}) {}\n".format(itemNumber, description[0]), 0.015)

    # pester user for correct input
    choice = None
    print()

    firstRun = True
    while choice is None:
        choice = menuItems.get(input(">> "))

        if choice is None:
            if firstRun:
                replaceLines(2)
                firstRun = False
            else:
                replaceLines(3)

            printS("\nInvalid Option!\n", 0.015, "red")

    # run selected function
    functionToRun = choice[1]  # get function address instead of description
    functionToRun()

    return


# update menu item dictionary
def addMenuItem(description, route):
    global menuItems

    itemNumber = len(menuItems) + 1
    menuItems.update({str(itemNumber): [str(description), route]})


def flushMenuItems():
    global menuItems
    menuItems = dict()


def getPassword():
    printS("Password: ", 0.03)

    password = ""
    while True:
        char = getch.getch()

        if char == "\n":  # enter was pressed
            break
        elif ord(char) == 127:  # backspace key was pressed
            if len(password) > 0:
                # erases previous character.
                sys.stdout.write("\b" + " " + "\b")
                sys.stdout.flush()
                password = password[:-1]
        else:
            sys.stdout.write("■")
            sys.stdout.flush()

            password += char

    # newline
    print()
    password = password.encode("utf-8")

    return hashlib.sha256(password).hexdigest()


def prompt(message, functionToRun=None, debug=False):
    printS("\n" + message + " [y/n]:", 0.015)
    choice = verifyInput(["y", "n"])

    if functionToRun is not None and choice == "y":
        functionToRun()
        return
    else:
        return choice


def cls():
    print("\n\n\n")  # so annoying text doesnt appear pon top
    os.system("clear")


def replaceLines(linesToDelete):
    cursorOneUp = "\x1b[1A"
    eraseLine = "\x1b[2K"

    for _ in range(linesToDelete):
        sys.stdout.write(cursorOneUp)
        sys.stdout.write(eraseLine)


def exit():
    enableEcho(True)
    printS("\nFarewell comrade\n", 0.015)
    sys.exit(0)


# from https://gist.github.com/kgriffs/5726314
def enableEcho(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)


# from
# https://stackoverflow.com/questions/26555070/linux-python-clear-input-buffer-before-raw-input
def flushInput():
    # common issue with enable_echo is that it doesnt actually disable input
    # therefore any input entered before prompt will be hidden but also will be registered
    # this function flushes that useless input, use before any text prompt that is
    # NOT using printS beforehand
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
