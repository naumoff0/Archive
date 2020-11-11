""" lockup for terminals """

import sys
import random
import termios

def lock(TIMEOUT_MODE=False):
    """ for naughty terminals"""
    try:
        while True:
            if TIMEOUT_MODE is True:
                std = list("CLOUD 9 EXCEPTION : OSError[12] Cannot Allocate Memory : RESTART REQUIRED")
                nonStd = []
                for _ in enumerate(std):
                    if random.randint(0, 3) == 0:
                        nonStd.append(chr(random.randint(1, 255)))

                    else:
                        nonStd.append(std[_])

                print("".join(nonStd), end="\r")

            print("".join(std), end="\r")

            print("\x1b[2K")

    except BaseException:
        lock(TIMEOUT_MODE=True)

def echo(enable):
    """ enables or disables echoing. from https://gist.github.com/kgriffs/5726314 """

    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)

    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)
