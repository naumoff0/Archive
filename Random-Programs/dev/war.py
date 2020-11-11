""" input """

import sys
import time
import random
import builtins
import linecache
import termcolor


def getSettings(setting):
    """ gets settings """
    if setting == "print":
        PRINT_SPEED = float(linecache.getline("settings.txt", 1).rstrip("\n"))
        return PRINT_SPEED

    elif setting == "names":
        CUSTOM_NAMES = linecache.getline("settings.txt", 2).rstrip("\n")

PRINT_SPEED = getSettings("print")
CUSTOM_NAMES = getSettings("names")

class human:
    """ a single squad member """
    def __init__(self):
        self.name = getName()
        self.hp = 10
        self.alive = True
        self.rolls = None

    def roll(self):
        """ roll the duce """
        self.rolls = random.randint(1, 20)


    def wound(self, wounder):
        """ wounds a human """
        if self.rolls < random.randint(1, 20):
            dmg = random.randint(1, 3)
            print("{} ".format(self.name), "yellow", "")
            print("was hit for ", None, "")
            print("[-{} hp]".format(dmg), "red", "")
            print("[{} hp]".format(self.hp - dmg), "green")
            print("{} ".format(self.name), "yellow", "")
            print("rolled {} to a {}".format(self.rolls, wounder.rolls))
            self.hp -= dmg

    def checkMyVitals(self): # :)
        """ *check my vital sigggns...* """
        if self.hp <= 0:
            print("\n\nFATALITY :: [{}] was killed\n\n".format(self.name), "red")
            self.alive = False

        else: return 0



class squad:
    """ full squad """
    def __init__(self):
        self.name = getName()
        self.members = [human(), human(), human(), human()]
        self.memberNames = []
        for item in self.members:
            self.memberNames.append(item.name)
        self.active = True

    def countOff(self):
        """ counts off members """
        print("{} squad count off".format(self.name))
        counter = 0
        for item in self.members:
            if item.alive is not True:
                del self.members[counter]
                del self.memberNames[counter]
            counter += 1

        for item in self.memberNames:
            print(item)

        print("\n")

    def checkActive(self):
        """ checks if anyone is still out there """
        if len(self.members) <= 0:
            print("{} is out of action".format(self.name))
            self.active = False


def getName():
    """ allows for random human names"""
    name = ""
    for _ in range(5):
        char = chr(random.randint(97, 122))
        if char != "\n":
            name += char

        else:
            name += " "

    return name


def combat(one, two, lengths):
    """ squad combat """
    if random.randint(0, 1) == 1:
        first = one
        last = two

    else:
        first = two
        last = one

    for i in range(lengths):
        personA = first.members[i]
        personB = last.members[i]
        print("[{}] v/s [{}]".format(personA.name, personB.name))

        while personA.hp > 0 and personB.hp > 0:
            personA.roll()
            personB.roll()
            if personA.rolls > personB.rolls:
                personB.wound(personA)

            else:
                personA.wound(personB)

            personA.checkMyVitals()
            personB.checkMyVitals()

def delayed_print(text, color=None, end=None):
    """ prints characters with delay provided between each character. color for prompt is optional """

    text = str(text)
    if end != "":
        text += "\n"
    for char in text:
        if color:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()
        time.sleep(PRINT_SPEED)




def main():
    """ main """

    builtins.print = delayed_print
    print("init [war.py]")
    print("enter to begin")
    input()
    while input("continue[y/n]").lower() != "n":
        one = squad()
        two = squad()
        while one.active is True and two.active is True:
            one.countOff()
            two.countOff()
            lengths1 = len(one.members)
            lengths2 = len(two.members)

            if lengths1 < lengths2:
                combat(one, two, lengths1)

            else:
                combat(one, two, lengths2)

            one.checkActive()
            two.checkActive()
            input("enter to continue round")



if __name__ == "__main__":
    main()
