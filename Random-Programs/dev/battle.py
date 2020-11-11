""" this program kills humans """
import sys
import time
import random
import builtins
import termcolor

PRINT_SPEED = 0.005
DEBUG_MODE = False

class human:
    """ a human exists... to die """
    def __init__(self, name):
        self.hp = 10
        self.incombat = False
        self.name = name
        self.advantage = getAdvantage()


    def checkWound(self):
        """ checks if a human is wounded """

        dmg = random.randint(1, 4)
        print("{} is hit".format(self.name), end="")
        time.sleep(.2)

        if random.randint(0, 100) > self.advantage:
            print(" [not wounded]", None, "green")

        else:

            if self.hp != 0:
                print(" [wounded][hp = {}]".format(self.hp - dmg), None, "red")

            elif self.hp <= 0:
                print(" [dead]")
            self.hp -= dmg


def remove_lines(amount):
    """ deletes lines printed previously """

    cursor_up = "\x1b[1A"
    erase = "\x1b[2K"

    for _ in range(amount):
        sys.stdout.write(cursor_up)
        sys.stdout.write(erase)


def delayed_print(text, end=None, color=None):
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
    time.sleep(PRINT_SPEED * 5)
def contest(other):
    """contests human ability"""
    return random.randint(1, 20) > round(other.advantage / 5)


def getAdvantage():
    """shut is advantage"""
    return random.randint(0, 100)


def hpBar(hp):
    """ returns an hp bar """
    ber = ""
    for _ in range(hp):
        ber += "#"
    for _ in range(10 - hp):
        ber += " "
    return "|" + ber + "|"


def getColor(hp):
    """ allows for specifically colored hp bars """
    if hp < 4:
        color = "red"
    if hp >= 4 and hp <= 7:
        color = "yellow"
    if hp > 7:
        color = "green"
    return color


def combat(playerOne, playerTwo):
    """full combat"""
    rounds = 0
    if playerOne.name == playerTwo.name:
        print("{} commits suicide".format(playerOne.name))
        return 1

    while playerOne.hp != 0 and playerTwo.hp != 0:
        combatRound(playerOne, playerTwo)
        rounds += 1
        if rounds % 10 == 0 and rounds != 0:
            print("We are taking a break!")
            print("{} hp:{}".format(playerOne.name, playerOne.hp))
            print("{} hp:{}".format(playerTwo.name, playerTwo.hp))
            time.sleep(3)
            remove_lines(3)

    if playerOne.hp <= 0:
        print("{} is dead, {} is is the champion".format(playerOne.name, playerTwo.name))
        print("combat took {} rounds".format(rounds))
        return 1

    else:
        print("{} is dead, {} is is the champion".format(playerTwo.name, playerOne.name))
        print("combat took {} rounds".format(rounds))
        return 2


def combatRound(playerOne, playerTwo):

    """single rounds of human to human combat"""
    hpOne = hpBar(playerOne.hp)
    hpTwo = hpBar(playerTwo.hp)
    colorOne = getColor(playerOne.hp)
    colorTwo = getColor(playerTwo.hp)
    print(playerOne.name)
    print("{}".format(hpOne), None, colorOne)
    print(playerTwo.name)
    print("{}".format(hpTwo), None, colorTwo)

    if random.randint(0, 1) == 1:
        success = contest(playerTwo)
        print("{} attacks {}".format(playerOne.name, playerTwo.name), end="")

        if success is True:
            print(" [success]")
            playerTwo.checkWound()

        else:
            print(" [failed]")
            successTwo = contest(playerOne)
            print("{} attacks {}".format(playerTwo.name, playerOne.name), end="")

            if successTwo is True:
                print(" [success]")
                playerOne.checkWound()

            else:
                print(" [failed]")
    else:
        success = contest(playerOne)
        print("{} attacks {}".format(playerTwo.name, playerOne.name), end="")

        if success is True:
            print(" [success]")
            playerOne.checkWound()

        else:
            print(" [failed]")
            successTwo = contest(playerTwo)
            print("{} attacks {}".format(playerOne.name, playerTwo.name), end="")

            if successTwo is True:
                print(" [success]")
                playerTwo.checkWound()

            else:
                print(" [failed]")

    print("[round over]")
    time.sleep(.5)

    if DEBUG_MODE is not True:
        remove_lines(10)


def spawn(name):
    """allows for human corpse overwriting"""
    bloo = human(name)
    return bloo


def main():
    """ main arena """
    builtins.print = delayed_print
    print("welcome to fight simulator")
    print("enter names of combatants")
    combatantOne = input("combatant one\n>> ")
    combatantTwo = input("combatant two\n>> ")
    remove_lines(6)
    combatantOne = spawn(combatantOne)
    combatantTwo = spawn(combatantTwo)

    while True:
        combatantOne.advantage = random.randint(25, 100)
        combatantTwo.advantage = random.randint(25, 100)
        result = combat(combatantOne, combatantTwo)

        if result == 1:
            combatantOne = spawn(input("new combatant\n>> "))
            combatantTwo.hp = 10

        elif result == 2:
            combatantTwo = spawn(input("new combatant\n>> "))
            combatantOne.hp = 10

if __name__ == "__main__":
    main()
