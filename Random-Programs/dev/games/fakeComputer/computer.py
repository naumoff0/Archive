import sys
import os
import time
import linecache

def create(text,delay,end):
    for p in text:
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(delay)
    if end == True:
        print('')

def createFile(fileName,fileExtn):
    with open('{}.{}'.format(fileName,fileExtn)) as file:
        print()
def editFile():
    print()
def deleteFile():
    print()
    
def main():
    direc = ''
    while True:
        create('TERMLINK PROTOCOL::CPYRGHT PTMSTUDIOS::RUNTIME ENVIRONMENT 0.0.8',0.05,True)
        create('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',0.01,True)
        create('SYS:{}\>'.format(direc),0.2,False)
        inpt = input('')
        if inpt == 'cd':
            create('SYS:CD\>',0.5,False)
            cd = input('')
            direc = cd
            cd = ''
        elif inpt == 'open':
            create('SYS:OPN\>',0.5,False)
            cd = input('')
        elif inpt == 'create':
            create('SYS:CRT\>',0.5,False)
            cd = input('')
        elif inpt == 'create':
            create('SYS:CD\>',0.5,False)
            cd = input('')
if __name__ == '__main__':
    main()