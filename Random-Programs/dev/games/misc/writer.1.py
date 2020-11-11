import time
import sys
from shutil import copyfile
#importing libraries
def main():
    num = int(input("amount: "))
    #getting user input for file name and amount
    while num > 0:
        clone = input("name of file created: ")
        cloneEX = input("cloned file extension:")
        template = input("cloned file name:")
        templateEX = input("cloned file extension:")
        copyfile("" + template + templateEX, "" + clone + cloneEX) #creates a file called ?????.py
        print("Finding Directories")
        time.sleep(1)
        print("Creating {}.py".format(clone))
        time.sleep(1)
        print("File successfully created")
        time.sleep(1)
        num -= 1
if __name__ == "__main__":
    main()