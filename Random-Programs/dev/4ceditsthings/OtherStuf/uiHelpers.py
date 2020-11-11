from collections import OrderedDict
from termcolor import colored
import linecache
import hashlib
import getch
import time
import sys
import os


menuItems = dict()


def printS(text, delay, color=None):
    for char in text:
        if color is not None:
            sys.stdout.write(colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()
        time.sleep(delay)


def verifyInput(acceptedInput):
    choice = input("\n>> ")

    while choice not in acceptedInput:
        printS(
            colored(
                "ERROR << input[{}] INVALID\n".format(choice), "red"), .02)
        printS(colored("ACCEPTED INPUT >> {}\n".format(
            acceptedInput), "green"), .02,)
        choice = input("\n\n>> ")

    return choice


def makeMenu(menuName, subHeader=None):
    cls()

    # print menu header and subheader if specified
    printS(menuName + "\n", 0.02)

    if (subHeader is not None):
        printS(subHeader, 0.02)

    # print line seprator for title
    for i in range(len(menuName) + 5):
        print("─", end="")

    print("")
    global menuItems

    # sort menu items by key so lowest is at top and then display them
    for itemNumber, description in sorted(menuItems.items()):
        # description is a mini list (description, route)
        printS("{}) {}\n".format(itemNumber, description[0]), .01)

    # pester user for correct input
    choice = None
    while choice is None:
        choice = menuItems.get(input("\n>> "))

        if choice is None:
            printS("Invalid Option!\n", .02, "red")

    # run selected function
    functionToRun = choice[1]  # get function address instead of description
    functionToRun()


# update menu item dictionary
def addMenuItem(description, route):
    global menuItems

    itemNumber = len(menuItems) + 1
    menuItems.update({str(itemNumber): [str(description), route]})


def flushMenuItems():
    global menuItems
    menuItems = dict()


def backToMenu():
    printS("Return back to main menu? [yes/no]\n", .02)
    choice = verifyInput(["y", "n", "yes", "no"])

    if choice.startswith("y") == False:
        printS("Farewell comrade.\n", .02)
        sys.exit(0)


def raiseIssue():
    printS("An Error Occured (enter DEBUG to see it).\n", .01, "red")
    printS(
        "Would you like to continue (warning, game might break) [yes/no]\n", .01, "red")

    quit = verifyInput(["y", "n", "yes", "no", "DEBUG"])

    if quit == "DEBUG":
        printS("EXCEPTION RAISED:\n\n", 0.02, "red")
        return True

    if quit.startswith("n"):
        sys.exit(0)


def getPassword():
    printS("Password: ", 0.02)

    password = ""
    while True:
        char = getch.getch()

        if char == "\n":
            break
        elif ord(char) == 127:  # backspace key
            if len(password) > 0:
                # erases previous character.
                sys.stdout.write("\b" + " " + "\b")
                sys.stdout.flush()
                password = password[:-1]
        else:
            sys.stdout.write("*")
            sys.stdout.flush()

            password += char

    # newline
    print()
    password = password.encode("utf-8")

    return hashlib.sha256(password).hexdigest()


def cls():
    os.system("cls" if os.name == "nt" else "clear")
