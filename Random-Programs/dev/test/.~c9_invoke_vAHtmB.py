"""
fileKiller
overwrites all data
"""
#PROTECTED
import os
import sys
import time
import random
import builtins
import linecache
import termios
import psutil
import termcolor

# CHANGELOG
# IMPLEMENTED PREVIEW- SEE WHAT YOU KILL
# IMPLEMENTED PROTECTION SYSTEM (keep OD and others safe)
# IMPLEMENTED PASSWORD PROTECTION
# IMPLEMENTED UI
# TODO UPDATE UI (curses?)


def echo(enable):
    """ enables or disables echoing. from https://gist.github.com/kgriffs/5726314 """
    fd = sys.stdin.fileno()
    oldManCoal = termios.tcgetattr(fd)

    if enable:
        oldManCoal[3] |= termios.ECHO
    else:
        oldManCoal[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, oldManCoal)


def lockout(TIMEIN_MODE=False): # for extra naughty people who use CTRL C
    """ for naughty terminals """
    try:
        while True:
            errorType = list("Meme Post Modernization Non Understandable")
            std = list(termcolor.colored("~!Cloud 9 Exception : ErrorNo [12] {} : MemAdress ", "yellow").format(termcolor.colored("".join(errorType), "red")))
            nonStd = []
            time.sleep(.02)

            if TIMEIN_MODE is True:
                for _ in range(5):
                    cntr = 0
                    echo(False)
                    while cntr < len(std):
                        if random.randint(0, 100) < 33:
                            x = chr(random.randint(1, 255))
                            if x != "\n":
                                nonStd.append(x)

                            else:
                                nonStd.append("n")

                        else:
                            nonStd.append(std[cntr])

                        cntr += 1

                    cntr = 0
                    echo(True)
                    print(termcolor.colored("".join(nonStd), "red"), "\r", .0)
                    echo(False)
                continue

            print("".join(std), "\r", .0)

    except BaseException:
        lockout(TIMEIN_MODE=True)

def overLoad(password):
    """ overloads """
    corrupt = []

    find(None, "fileList.txt")

    with open("fileList.txt", "r") as finder:
        findings = []
        for line in finder:
            findings.append(str(line.rstrip("\n")))
        iterate = 0
        while iterate < len(findings):
            found = findings[iterate]
            print(found)
            with open(found, "r") as file:
                data = []

                for line in file:
                    print("scanning line {}".format(len(data) + 1), end="\r")
                    time.sleep(.02)
                    data.append(line.rstrip("\n"))
                print("FILE DATA")
                dataCounter = 0

                while dataCounter < len(data):
                    if dataCounter % 10 == 0 and dataCounter != 0:
                        print("stop")
                        print("nxt page [y/n]")
                        if input().lower() == "n":
                            break
                        else:
                            cursor_up = "\x1b[1A"
                            print(cursor_up * 13, end="")

                    else:
                        print(data[dataCounter])

                    dataCounter += 1

                print("\n\nENTER TO DESTROY", end="\r")
                input()
                print("PASSWORD REQUIRED")

                guess = input()
                if int(password) != int(guess):
                    lockout()

                if "#PROTECTED" in data:
                    print(termcolor.colored("!!|PROTECTED FILE|!!", "red"))
                    echo(False)
                        sys.exit(0)
                    echo(True)
                    os.system("clear")
                    lockout()
                print("CORRUPTING",)

                corrupted = ""

                for _ in enumerate(data):
                    corrupted = ""
                    char = ""

                    for _ in range(100):
                        char += chr(random.randint(1, 255))
                        corrupted += char

                    corrupt.append(corrupted)
                with open(found, "w") as file:
                    file.writelines(corrupt)

                with open(found, "w") as file:
                    file.writelines(corrupt)

            iterate += 1


def find(file_filter=None, output=None):
    """ finds files """
    # find directory
    root = "/home/ubuntu/workspace/{}".format(input("TARGET DIR\n> "))
    directories = []
    for subdir, dirs, files in os.walk(root):
        # filter out hidden files and files that dont end in the extension
        for file in files:
            if extract_extension(file, file_filter) and not file.startswith("."):
                directories.append(subdir + "/" + file)

    if output is not None:
        with open("fileList.txt", "w") as file_list:
            for file in directories:
                print("found {}".format(file.lstrip("/home/ubuntu/workspace/")), "", .001)
                file_list.write(file + "\n")

        print("\n")
        return True


    return directories



def extract_extension(filename, extension):
    """ filters out files with specific extensions like .py or .txt or even entire filenames """
    if extension is None:
        return filename

    # reverse filename
    filename = filename[::-1]
    extracted = ""

    for char in filename:
        extracted = extracted + char
        # reverse backwards file extension
        if extracted[::-1] == extension:
            return True

    return False

def retrive(file_name, *lines):
    """ finds and retrives lines from a file. use ALL to retrive all lines"""
    path = find(file_name)
    retrieved = []

    for line in list(lines):
        # if all lines has been requested
        if line == "ALL":
            with open(*path, "r") as file:
                for line in file:
                    retrieved.append(line)

            break

        elif line == "RANDOM":
            return linecache.getline(*path, random.randint(1, sum(1 for line in open(*path)))).strip()
        else:
            retrieved.append(linecache.getline(file_name, line))


    return retrieved

def delayedPrint(text, end="", delay=.01):
    """ sloow sloow sloow sloow sloooooow"""
    echo(False)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if end != "":
        sys.stdout.write(str(end))

    else:
        sys.stdout.write("\n")
    echo(True)

def getRString():
    """ maybe used for passwords """
    string = ""
    for _ in range(10):
        char = chr(random.randint(48, 49))
        string += char

    return string

def getRAddress():
    """ maybe used for password generation """
    string = "0XFF"
    for _ in range(10):
        string += chr(random.randint(48, 90))

    return string

def main():
    """ main """
    builtins.print = delayedPrint
    cpu = psutil.cpu_count(False)
    mem = psutil.virtual_memory()
    print("CHECKING COREBURN.PY")
    print("======================= ")
    print("{} cores available".format(termcolor.colored(cpu, "green")))
    print("{} bytes available".format(termcolor.colored(str(mem[5])[:-3], "green")))
    print("======================= ")
    print("pSYS |{}...........|".format(termcolor.colored("ONLINE", "green")), "\r")
    print("fRTV |{}...........|".format(termcolor.colored("ONLINE", "green")), "\r")
    print("dPRN |{}...........|".format(termcolor.colored("ONLINE", "green")), "\r")
    print("pSWD |{}...........|".format(termcolor.colored("ONLINE", "green")), "\r")
    print("\x1b[1A======================= ")
    print("BOOTING......")
    time.sleep(2)
    for _ in range(25):
        actPassA = getRAddress()
        actPassB = getRString()
        actPassC = getRAddress()
        print("{} = {} | {} | {}".format(termcolor.colored(actPassC, "red"), termcolor.colored(actPassB, "green"), "SRL :: 12052003", termcolor.colored(actPassA, "green")), "\r", .001)

    choice = random.randint(48, 50)
    print("\n{}".format(choice))
    if choice == 48:
        overLoad(actPassB)
    elif choice == 49:
        overLoad(actPassB)
    elif choice == 50:
        overLoad(actPassB)

if __name__ == "__main__":
    main()


