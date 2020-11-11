""" lockup for terminals """

import os
import sys
import time
import random
import termios
import termcolor

def echo(enable):
    """ enables or disables echoing. from https://gist.github.com/kgriffs/5726314 """

    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)

    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)


def lock(TIMEOUT_MODE=False): # for extra naughty people who use CTRL C
    """ for naughty terminals """
    try:
        while True:
            errorType = list("Mem Allocation")
            std = list(termcolor.colored("~!Cloud 9 Exception : ErrorNo [12] {} : MemAdress ", "yellow").format(termcolor.colored("".join(errorType), "red")))
            nonStd = []
            time.sleep(.02)

            if TIMEOUT_MODE is True:
                cntr = 0
                echo(False)
                while cntr < len(std):
                    if random.randint(0, 3) == 0:
                        x = chr(random.randint(1, 255))
                        if x != "\n":
                            nonStd.append(x)

                        else:
                            nonStd.append("n")

                    else:
                        nonStd.append(std[cntr])

                    cntr += 1

                cntr = 0
                echo(True)
                print(termcolor.colored("".join(nonStd), "red"), end="\r")
                echo(False)
                # cursors down three lines, deletes three lines, returns back to top ten times
                for _ in range(10):
                    print("\n\n\n\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A\x1b[2K", end="\r")
                continue

            print("".join(std), end="\r")
            os.system("clear")

    except BaseException:
        lock(TIMEOUT_MODE=True)

lock()
