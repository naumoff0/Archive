import random
import time
import getch
import sys
import os

def scannerator():
    scanstrip = ""
    for i in range(10):
        rando = random.randint(0,3)
        if rando != 0:
            scanstrip += ("#")
        else:
            scanstrip += ("-")
    scanstrip = "|" + scanstrip + "|"
    return scanstrip.rstrip("\n") 

def equate(integer1, operand, integer2):
    if operand == "+":
        return integer1 + integer2
    elif operand == "-":
        return integer1 - integer2
    elif operand == "*":
        return integer1 * integer2
    elif operand == "/":
        return integer1 / integer2



def evaluate(line):
    try:
        segmented = list(line)
        ints = []
        operands = []
        currentInt = ""
        x = 0
    
        for item in segmented:
            if str(segmented[x]) in list("1234567890"): currentInt += segmented[x]
    
            elif segmented[x] in list("*^/+-"):
                if currentInt != "":
                    ints.append(currentInt)
                    currentInt = ""
                operands.append(segmented[x])
                
            x += 1
            
        if currentInt != "": ints.append(currentInt)
        
        carryover = ""
        intsUsed = 0
        counter = 0
        
        while counter < len(operands):
            if len(operands) - counter > 1:
                if operands[counter] in list("+-") and operands[counter + 1] in list("*/"):
                    if carryover == "":
                        int1 = ints[intsUsed]
                        int2 = ints[intsUsed + 1]
                        intsUsed += 2
                        
                    elif carryover != "":
                        int1 = int(carryover)
                        int2 = ints[intsUsed]
                        intsUsed += 1
                        
                    operand = operands[counter]
                    carryover = equate(int1, operand, int2)
            
            elif len(operands) - counter == 1:
                
                int1 = int(carryover)
                int2 = ints[intsUsed]
                operand = operands[counter]
                carryover = equate(int1, operand, int2)
                
                print(carryover)
                
            
                
            
            counter += 1
        
    except (IndexError, ValueError):
        print("ERROR: SYNTAX")
             
        
        

def main():
    try:
        line = ""
        while True:
            linefrag = getch.getch()
            if linefrag == "\n":
                print("\n")
                scannerator()
                evaluate(line)
                line = ""
                os.system("clear")
                print("Calcalator 2000")
                print("-" * len(line))
                print("A For Special Sequences")
                print("-" * len(line))
                line = ""
    
            elif linefrag in list("+-/*1234567890"):
                line += linefrag
                sys.stdout.write(linefrag)
                sys.stdout.flush()
            elif ord(linefrag) == 127:
                if len(line) > 0:
                    sys.stdout.write("\b" + " " + "\b")
                    sys.stdout.flush()
            elif linefrag == "a":
                print("_______\n1)Root\n2)Quadratic\n3)MX+B")
                chc = int(input(">> "))
                if chc == 1: print(squareRoot(float(input("Original Number\n>> ")), float(input("Root by\n>> "))))
                elif chc == 2: rootQuadratic(float(input("a =\n>> ")), float(input("b =\n>> ")), float(input("c =\n>> ")))
                elif chc == 3: MXB(float(input("X Of Point 1\n>> ")), float(input("Y Of Point 1\n>> ")), float(input("X Of Point 2\n>> ")), float(input("Y Of Point 2\n>> "))
                
    except ValueError:
        print("ERROR: INPUT")



def rootQuadratic(a, b, c):
    #calculates and displays x intercepts and vertex
    print("j is a complex number")
    xRootA = (-b + squareRoot((b ** 2) - 4 * (a * c), 2)) / (a * 2)
    print("x root A is equal to >> {}\n".format(xRootA))
    xRootB = (-b - squareRoot((b ** 2) - 4 * (a * c), 2)) / (a * 2)
    print("x root B is equal to >> {}\n".format(xRootB))
    xVertex = (xRootA + xRootB) / 2
    yVertex = (a  * xVertex) ** 2 + b * xVertex + c
    print("vertex coordinates are ({},{})".format(xVertex, yVertex))
    print("enter to continue")
    a = input("")
    

def MXB(p1X, p1Y, p2X, p2Y):
    try:
        #calculates and displays y = mx + b equation given two points
        dY = p1Y - p2Y
        dX = p1X - p2X
        sL = dY / dX
        b = p1Y - sL * p1X
        print("y = {}x + {}".format(sL, b))
        print("enter to continue")
        a = input("")
    
    except ZeroDivisionError:
        print("ERROR: ZERODIVISIONERROR")
    

def squareRoot(original, squareBy):
    for i in range(100):
        print("{}".format(scannerator()), end = "\r")
        time.sleep(0.01)
    print("|---DONE---|")
    sqrt = original ** (1 / squareBy)
    return sqrt


if __name__ == "__main__":
    main()