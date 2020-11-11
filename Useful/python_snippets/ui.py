""" user interface module """
import codecs
import os
import sys
import time
from collections import OrderedDict

import termcolor

CLEAR_SCREEN = True
PRINT_SPEED = 0.015
COLOR = True


def delayed_print(text, color=None):
    """ prints characters with delay provided between each character. color for prompt is optional """

    for char in str(text):
        if color and COLOR:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()
        time.sleep(PRINT_SPEED)


def accepted_input(*accepted):
    """ ensures user provides input that is accepted """

    accepted = [str(s) for s in accepted]
    choice = input("\n>> ")

    while choice not in accepted:
        remove_lines(1)
        print("Invalid! >> ", "red")
        choice = input()

    return choice


def prompt(message, function, *args):
    """ prompts user with y/n. if function is provided and the users answers y, the function will be executed"""

    print(str(message) + " [y/n]:")
    choice = accepted_input("y", "n")

    if function and choice == "y":
        function(*args)

    if choice == "n":
        return False

    return True


def clr():
    """ clears the terminal """
    if CLEAR_SCREEN:
        os.system("cls" if os.name=="nt" else "clear")


def remove_lines(amount):
    """ deletes lines printed previously """

    cursor_up = "\x1b[1A"
    erase = "\x1b[2K"

    for _ in range(amount):
        sys.stdout.write(cursor_up)
        sys.stdout.write(erase)


class Menu(object):
    """ displays a numbered menu with optional prompt. if an item is selected, the function corresponding to that item will be executed """

    def __init__(self, header=None):
        self.header = header
        self.options = OrderedDict()

    def add(self, description, route="", *args):
        """ adds an option to the menu. """

        option_number = len(self.options) + 1 # menus start at 1
        self.options.update({str(option_number): [str(description), route, args]})

    def display(self, menu_prompt=True):
        """ displays all options in a menu """

        clr()
        print(self.header + "\n")
        print("-----------------\n")

        # display options
        for option_number, description in self.options.items():
            print("{}) {}\n".format(option_number, description[0]))

        if menu_prompt:
            choice = self.options.get(input("\n>> "))
            while not choice:
                remove_lines(1)
                print("Invalid! >> ", "red")
                choice = self.options.get(input())

            if choice[1]:
                # function address and args
                choice[1](*choice[2])

            self.exit()

        return

    def exit(self):
        """ ask user if they want to quit """

        if not prompt("\nReturn back to menu?", None):
            raise SystemExit

        self.display()
