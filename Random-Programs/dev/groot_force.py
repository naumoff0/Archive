""" brute force module """
import time
import random


def get_message():
    """ this retrives message from user """

    target = list(input("TARGET MESSAGE: \n> ").lower())

    message = []
    successes = 0
    while "".join(message) is not "".join(target):
        char = ""
        while True: # default for now
            char = chr(32, 126)
            print("", end=char)
            if char != target[1]:
                


get_message()
