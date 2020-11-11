import linecache
import time
import sys

def printS(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.02)
        
        
def printThePlay():
    printS("ENTER TO PRINT THE PLAY")
    input()
    counter = 0
    with open ("play.txt", "r") as file:
        for line in file:
            line = linecache.getline("play.txt", counter + 1)
            for i in range(10):
                line = line.rstrip("\n")
            line += "\n"
            printS(line)
            counter += 1
            
printThePlay()