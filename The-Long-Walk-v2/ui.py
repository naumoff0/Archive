from collections import OrderedDict
import random
import time
import sys
import os

import termcolor
import linecache

import entity
import game
import main


PLAYER_INSANITY = 0
CLEAR_SCREEN = True
PRINT_SPEED = 0


def update_insanity(insanity):
    """ updates the insanity variable """
    global PLAYER_INSANITY
    PLAYER_INSANITY = insanity


def set_print_speed(set_val):
    """ sets print speed to a certain value, lower is faster """
    global PRINT_SPEED
    PRINT_SPEED = set_val


def delayed_print(text, color=None):
    """ prints characters with delay provided between each character. color for prompt is optional """
    for char in str(text):
        char = char.encode("utf8").decode(sys.stdout.encoding)
        if char == " ":
            sys.stdout.write(char)
            continue

        if random.randint(0, 300) < PLAYER_INSANITY:
            sys.stdout.write(termcolor.colored(chr(random.randint(ord(char) - 10, ord(char) + 10) ).encode("utf8").decode(sys.stdout.encoding), color))
        
        elif color != True:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)
        
        # flush the input buffer based on os
        if os.name == "nt":
            while msvcrt.kbhit():
                msvcrt.getch()
        else:
            sys.stdout.flush()
        
        time.sleep(PRINT_SPEED)


def clr():
    """ clears the terminal """
    if CLEAR_SCREEN:
        os.system("cls" if os.name == "nt" else "clear")


def remove_lines(amount):
    """ deletes lines printed previously """

    cursor_up = "\x1b[1A"
    erase = "\x1b[2K"

    for _ in range(amount):
        sys.stdout.write(cursor_up)
        sys.stdout.write(erase)