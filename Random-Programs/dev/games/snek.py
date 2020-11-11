from random import randint
import linecache
import time
import sys
import os


def getFrame(location):
    l0 = list(linecache.getline("arena.txt", 1))
    l1 = list(linecache.getline("arena.txt", 2))
    l2 = list(linecache.getline("arena.txt", 3))
    l3 = list(linecache.getline("arena.txt", 4))
    l4 = list(linecache.getline("arena.txt", 5))
    l5 = list(linecache.getline("arena.txt", 6))
    l6 = list(linecache.getline("arena.txt", 7))
    l7 = list(linecache.getline("arena.txt", 8))
    l8 = list(linecache.getline("arena.txt", 9))
    l9 = list(linecache.getline("arena.txt", 0))
    
    if location[0] == "0":
        l0[location[1]] = "@"
        
    elif location[0] == "1":
        l1[location[1]] = "@"
        
    elif location[0] == "2":
        l2[location[1]] = "@"
        
    elif location[0] == "3":
        l3[location[1]] = "@"
        
    elif location[0] == "4":
        l4[location[1]] = "@"
        
    elif location[0] == "5":
        l5[location[1]] = "@"
        
    elif location[0] == "6":
        l6[location[1]] = "@"
        
    elif location[0] == "7":
        l7[location[1]] = "@"
        
    elif location[0] == "8":
        l8[location[1]] = "@"
        
    elif location[0] == "9":
        l9[location[1]] = "@"
        
    print("".join(l0) + "".join(l1) + "".join(l2) + "".join(l3) + "".join(l4) + "".join(l5) + "".join(l6) + "".join(l7) + "".join(l8) + "".join(l9))
    
    
    
    
while True:    
    testLocations = list("0123456789")
    getFrame([testLocations[randint(0, 9)], 3])
    