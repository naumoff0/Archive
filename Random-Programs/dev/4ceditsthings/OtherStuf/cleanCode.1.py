from uiHelpers import *
import subprocess
import sys
import os


def cleanCode():
    printS("Cleaning process initiated\n\n", 0.02)
    filesCleaned = 0
    totalFiles = 0
    
    with open("fileList.txt", "r") as file:
        for line in file:
            if line.find(".py") != -1:  # python file found
                totalFiles += 1
                # extract filename which ends at /
                lastChar = len(line) - 1
                extractedFilename = ""

                i = 0
                while True:
                    # ensure source directory OD/ isnt added
                    if line[lastChar - i] == "/":
                        if line[lastChar - (i + 1)] == "D":
                            if line[lastChar - (i + 2)] == "O":
                                break

                    extractedFilename += line[lastChar - i]
                    i += 1

                # reverse string  since filename was added backwards
                extractedFilename = extractedFilename[::-1]

                # silence subprocess output
                FNULL = open(os.devnull, "w")

                subprocess.call(
                    "autopep8 --in-place --aggressive --aggressive " +
                    extractedFilename,
                    shell=True,
                    stdout=FNULL,
                    stderr=subprocess.STDOUT)
            
                    
                    
                coloredFilename = colored(extractedFilename.rstrip("\n"), "green")
                sys.stdout.write("File Cleaned: {} :[{}%]\r".format(coloredFilename, 10 * (filesCleaned / totalFiles)))
                sys.stdout.flush()
                
                filesCleaned += 1
                

    printS("\n\nDone!\n", 0.03, "green")

def main():
    cleanCode()
    
if __name__ == "__main__":
    main()