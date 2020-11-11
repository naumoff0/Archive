import linecache
import time
import sys
import os
from random import randint


def getLine(fileName):
    num_lines = sum(1 for line in open(fileName))
    line = linecache.getline(fileName, randint(1, num_lines))
    return line.rstrip()
    
    
def printSeparately(text,delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    print("")
        
        
def getSong(leng, delay):
    os.system('clear') 
    
    print("{}, a Russian Epic \nWritten By {}!\n________________________\n".format(getLine("titles.txt"), getLine("names.txt")))
    
    for i in range(leng):
        line  = getLine('russianFolkSongs.txt')
        printSeparately(line, delay)
        
        if randint(1, 100) < 30:
            print("")
            
            
def main():
    knownSongs = ["russianFolkSongs.txt"]
    
    while True:
        try:
            songLength = int(input("Give number of lines comrade\n>> "))
            delay = int(input("Speed of typing (more=slower)\n>> "))
            delay = delay / 100
            
            if songLength < 1:
                print("No turnips to give.")
                continue
        except ValueError:
            print("Огонь!!!")
        else:
            break
        
    getSong(songLength, delay)
    
    
if __name__ == "__main__":
    main()