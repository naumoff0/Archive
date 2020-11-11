import time
import progressbar


def cls():
    print(chr(27) + "[2J")


def uInput(aIn):
    chc = input(">> ")
    while chc not in aIn:
        print("err > {} err.input".format(chc))
        print("accepted inputs >>> {}".format(aIn))
        chc = input(">> ")
    return chc


def bar(lngth, delay):
    bar = progressbar.ProgressBar()
    
    for i in bar(range(lngth)):
        time.sleep(delay)