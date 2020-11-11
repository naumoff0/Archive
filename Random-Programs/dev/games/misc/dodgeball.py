from random import randint
import time
from uiaddons import *
import linecache

def throw():
    if ballAvailible == True:
        print("You hurl the ball at {}".format(name))
        hit = randint(0,100)
        dgd = 100 * run
        uHit = randint(0,dgd)
        if uHit < dgd / (run * 2):
            print("before you can throw, a ball hits you in the face.")
            print("you are OUT!")
            dead = True
            return dead
        if hit > 50:
            print("You hit {}".format(name,))
            dead = False
    if ballAvailible == False:
        print("You don't have a ball")
        
def run():
    print("you run from the ball hurtling torwards you...")
    run = 2
    dgd = 100 * run
    uHit = randint(0,dgd)
    if uHit < dgd / (run * 2):
        print("your dodge is futile...")
        print("you are OUT")
        dead = True
        return dead
    print("you successfully dodge the ball!")
    dead = None
    return dead
                
def getName():
    name = linecache.getline("names.txt",randint(0,19))
    return name
def gameTurn(team1,team2):
    thrownAt = False
    ballAvailible = True
    name = getName()
    dead = None
    run = 1
    rando = randint(0,100)
    if rando < 35:
        thrownAt = True
    print("you are on the court")
    print("make a choice")
    if thrownAt == True:
        print("a ball has been thrown at you!")
        print("[throw(t)/run(r)/dodge(d)/catch(c)]")
        chc = uInput(["t","T","r","R","d","D","c","C"])
        if chc == "t" or chc == "T":
            throw()
        elif chc == "r" or chc == "R":
            run()
        elif chc == "d" or chc == "D":
            print("you attempt an awesome ninja dodge...")
            dgd = randint(0,100)
            if dgd > 75:
                print("your dodge is futile...")
                dead = True
                return dead
            print("You do the matrix on the ball...")
            dead = None
            return dead
        elif chc == "c" or chc == "C":
            print("you prepare to catch the ball...")
            ctch = randint(0,100)
            if ctch < 50:
                print("you catch the ball!")
                print("someone on B Team is out!")
                dead = False
                return dead
            elif ctch >= 51:
                print("you fumble the ball...")
                print("OUT!")
                dead = True
                return dead
            return dead
    elif thrownAt == False:
        print("[throw(t)/run(r)]")
    chc = uInput(["t","T","r","R"])
    if chc == "t" or chc == "T":
        if ballAvailible == True:
            print("You hurl the ball at {}".format(name))
            hit = randint(0,100)
            if hit > 50:
                print("You hit {}".format(name,))
                dead = False
        elif ballAvailible == False:
            print("you don't have a ball")
    elif chc == "r" or chc == "R":
        print("you run to a ball")
        return 1
    return dead
    
def main():
    print("welcome to the dodgeball court")
    print("enter the court")
    print("[y/n]")
    chc = uInput(["y","Y","n","N"])
    if chc == "y" or chc == "Y":
        A = 100
        B = 100
        ball = 0
        while True:
            print("processing...")
            bar(randint(100,1000),0.000001)
            happened = gameTurn(A,B)
            if happened == None:
                print("No players hit")
            elif  happened == True:
                print("A Team Player hit")
                A -= 1
            elif happened == False:
                print("B Team Player hit")
                B -= 1
            elif happened == 1:
                A += 1
            print("A Team Lives > {}".format(A))
            print("B Team Lives > {}".format(B))
            input("enter to end turn")
            cls()
            if A == 0:
                print("Team A Loses The Game")
                input("enter to end game")
                break
if __name__ == "__main__":
    main()