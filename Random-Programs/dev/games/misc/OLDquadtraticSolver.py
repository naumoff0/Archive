import time 
import sys
from math import sqrt


def main():
    # check if user has python 3
    if sys.version_info[0] < 3:
        print("You must have python 3 installed!")
        print("If you have python 3 installed, try running with: python3 Exurrb-Battle-Simulator.py if your using the command line")
        sys.exit(1)      
    
    while True:
        try:
            a = int(input("Value A: "))       
            b = int(input("Value B: "))       
            c = int(input("Value C: ")) 
        except ValueError:
            print("INVALID NUMBA")
        else:
            break
    
    if a == 0:
        print("A can not be zero!")
        sys.exit(1)
    else:
        getRoots(a, b, c)
        
        
def getRoots(a, b, c):
    try:
        # all of them parentheses
        xRoot1 = ((b * -1)+(sqrt((b**2) - (4 * a * c)))) / (2 * a)
        xRoot2 = ((b * -1)-(sqrt((b**2) - (4 * a * c)))) / (2 * a)
    except ValueError:
        print("\nNot Solvable or Equation contains complex roots.")
        sys.exit(2)
        
    print("________________________________")
    print("X root 1 is: {:.4f}".format(xRoot1))
    print("X root 2 is: {:.4f}".format(xRoot2))
    

if __name__ == "__main__":
    main()