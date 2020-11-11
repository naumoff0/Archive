import sys
import time
import termcolor
import progressbar
from random import randint


def preprint(assignLength, text = "", color = None):
    charAssigns = []
    intAssigns = []
    finalPrePrint = []
    for i in range(round(assignLength * 0.66)):
        x = randint(65, 90)
        charAssigns.append(chr(x))
    for q in range(round(assignLength * 0.33)):
        x = randint(48, 57)
        intAssigns.append(chr(x))
    for w in range(assignLength):
        x = randint(0, 1)
        if len(charAssigns) == 0:
            x = 0
        
        elif len(charAssigns):
            y = randint(0, len(charAssigns) - 1)
            
        if len(intAssigns) == 0:
            x = 1
            
        elif len(intAssigns):
            z = randint(0, len(intAssigns) - 1)
            
        if x == 1:
            finalPrePrint.append(charAssigns[y])
            charAssigns.remove(charAssigns[y])
            
        elif x == 0:
            finalPrePrint.append(intAssigns[z])
            intAssigns.remove(intAssigns[z])
            
    print("".join(finalPrePrint) + ":", end = "")


def printS(text, delay, color = None, preTag = 3):
    preprint(preTag, "", color)
    #delayed text output
    for char in text:
        if color != None:
            sys.stdout.write(char)
        else:
            sys.stdout.write(termcolor.colored(char, color))
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
    

def cls():
    #clearing screen for inputs, etc
    print(chr(27) + "[2J")
    