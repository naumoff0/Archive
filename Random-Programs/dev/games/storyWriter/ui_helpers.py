import sys
import time
import termcolor
import progressbar


def printS(text, delay, color = None): 
    #delayed text output
    for char in text:
        if color != None:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        

def uInput(acceptedInput):
    #input handler
    choice = input(">> ")
    while choice.lower() not in acceptedInput:
        printS("err > err.input[{}]\n".format(choice), .02, "red")
        printS("acptdInpt > [{}]\n".format(acceptedInput), .02, "green")
        choice = input(">> ")
    return choice


def bar(length, delay):
    #progress bars for loading
    bar = progressbar.ProgressBar()
    for i in bar(range(length)):
        time.sleep(delay)


def cls():
    #clearing screen for inputs, etc
    print(chr(27) + "[2J")
    