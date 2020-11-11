from math import sqrt
import sys
import os
from mathness import *
def main():
    lol = "mehbe"
    while lol == 'mehbe' or lol == "yes" or lol == "Yes":
        print("Menu")
        print("~~~~~~~~~~~~")
        print("1) Simple Maths")
        print("2) Complex Maths")
        print("3) Exit")
        chc = int(input(">> "))
        if chc == 2:
            print("Menu")
            print("1) Solve a quadratic equation")
            print("2) Solve a y = mx + b equation")
            print("5) Solve an algebraic equation")
            chc = int(input(">> "))
            if chc == 1:
                QUADEQ()
            elif chc == 2:
                YMXB()
            elif chc == 3:
                print("Non implemented...")
            print("Continue?")
            print("Yes")
        lol == str(input(">> "))
    
if __name__ == "__main__":
    main()