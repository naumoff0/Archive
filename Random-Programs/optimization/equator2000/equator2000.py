import cmath
import math
import time
from ui_helpers import *

        
        
def main():
    while True:s
        cls()
        printS("welcome to the equator\n", .04)
        printS("choose an equation\n", .04)
        chc = uInput(["LINE", "QUAD", "line", "quad"])
        if chc.lower() == "line":
            p1X = float(input("x of point 1\n>> "))
            p2X = float(input("x of point 2\n>> "))
            p1Y = float(input("y of point 1\n>> "))
            p2Y = float(input("y of point 2\n>> "))
            MXB(p1X, p1Y, p2X, p2Y)
        elif chc.lower() == "quad":
            a = float(input("a = ?\n>> "))
            b = float(input("b = ?\n>> "))
            c = float(input("c = ?\n>> "))
            rootQuadratic(a, b, c)
    
    
def rootQuadratic(a, b, c):
    #calculates and displays x intercepts and vertex
    printS("j is a complex number\n",.04)
    xRootA = -b + cmath.sqrt((b ** 2) - 4 * (a * c))
    printS("x root A is equal to >> {}\n".format(xRootA), .04)
    xRootB = -b - cmath.sqrt((b ** 2) - 4 * (a * c))
    printS("x root B is equal to >> {}\n".format(xRootB) ,.04)
    xVertex = (xRootA + xRootB) / 2
    yVertex = (a  * xVertex) ** 2 + b * xVertex + c
    print("vertex coordinates are ({},{})\n".format(xVertex, yVertex))
    printS("enter to continue",.04)
    a = input("")
    

def MXB(p1X, p1Y, p2X, p2Y):
    #calculates and displays y = mx + b equation given two points
    dY = p1Y - p2Y
    dX = p1X - p2X
    sL = dY / dX
    b = p1Y - sL * p1X
    printS("y = {}x + {}\n".format(sL, b),.04)
    printS("enter to continue",.04)
    a = input("")

if __name__ == "__main__":
    main()