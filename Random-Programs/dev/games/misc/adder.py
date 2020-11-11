import time
from random import randint
from uiaddons import *

def loadinBar(lngth,prgrss,loaded,ret1,ret2,pointer,complete,empty):
    #visual representation of the loading progress
    arr = prgrss
    dot = lngth - prgrss
    print("{}{}%{} {} {}".format(ret1,loaded,ret2,pointer,ret1), end = "")
    counter = 0
    while counter < arr:
        print("{}".format(complete), end = "")
        counter += 1
    cntr = 0
    while cntr < dot:
        print("{}".format(empty), end = "")
        cntr += 1
    print(ret2)
    
    
def add(num1,num2):
    contemplationTime = num1 + num2
    contemplationPerSecondModifier = num1 / num2
    print("Considering...")
    time.sleep(0.5)
    print("Preparing Contemplation...")
    time.sleep(0.5)
    counter = 0
    while counter <= 100:
        cls()
        print("Thinking...")
        if counter == 100:
            loadinBar(10,10,100,"[","]",">>","#"," ")
            print("done!")
            break
        loadinBar(10,(counter / 10),counter + 1,"[","]",">>","#"," ")
        time.sleep(0.2)
        counter += 1
    print("answers point to 42 rosemary bushes!")
    
    
def main():
    print("welcome to adder")
    print("first thing to add?")
    thing1 = intInput()
    print("second thing to add?")
    thing2 = intInput()
    add(thing1,thing2)
if __name__ == "__main__":
    main()