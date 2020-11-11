import sys
import os
import time
from ui_helpers import *


def checkPen(quality):
    printS("scanning for pen...\n", .05)
    if quality <= .75:
        printS("\tFOUND\n", .05, 'green')
    elif quality > .75:
        printS("\tBROKEN\n", .05, 'red')
        checkPen(quality - .4)

        
def checkPaper(length):
    printS("checking paper length...\n", .05)
    printS("\t{} LINES\n".format(length), .05, 'green')