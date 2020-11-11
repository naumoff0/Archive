from init import *
from ui_helpers import *
from structure import *
from random import randint


def main():
    penQuality = '0.'  + str(randint(0,99))
    checkPen(float(penQuality))
    paper = randint(1,100)
    checkPaper(paper)
    for i in range(round(paper / 2)):
        print("\t", end = "")
        passSubject = constructSimpleClause()
        printS('and then....\n', .02)
        constructSimpleClause(passSubject)
        print("\n")
if __name__ == "__main__":
    main()