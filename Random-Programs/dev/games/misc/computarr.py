import time
import sys
import os
from random import randint
#imports
def fail():
    #defining computer failure
    print("FATAL_ERROR:: {} strings unhandled".format(randint(1, 100)))
    time.sleep(1)
    print("Attempting to handle strings")
    time.sleep(1)
    print("Could not decorrupt streams")
    time.sleep(1)
    print("Deleting system32 in:")
    time.sleep(0.3)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Done!")
    
def main():
    direct = '/>'
    adminEnabled = 'no'
    adminIP = '14.754.01'
    adminPass = 'SecterForce22'
    while True:
        sysFold = 'system32'
        print("This is a file explorer")
        print("dont enter \"./delete.bat -i @ {}\"".format(sysFold))
        print("if you do bad things will happen")
        doIT = input("C:{}".format(direct))
        if doIT == "./delete.bat -i @ system32":
            # YOU DID THE THING!!!!!!!!!!
            fail()
            break
        if doIT == "cd":
            print("Directory?")
            directChange = input('Directory:')
            direct = directChange + '/>'
        if doIT == './net user -m push admin':
            adminEnabled == 'yes'
            print("admin enabled")
        if doIT == './net user -i info @ admin' and adminEnabled == 'yes':
            print("{}".format(adminIP))
        if doIT == './ipconfig push ufoNET @' + adminIP:
            print("{}".format(adminPass))
        if doIT == './force LOGIN admin @ pass:' + adminPass:
            print('access granted')
if __name__ == "__main__":
    main()