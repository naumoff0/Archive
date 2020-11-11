""" entity module """
from collections import OrderedDict
import random
import getch
import time
import os

import camping
import game
import ui



class Player:
    """ base self class """
    def __init__(self):
        self.ordered_attributes = OrderedDict()

        self.hp            = 20
        self.distance_travelled = 0

        self.exhaustion    = 0
        self.starvation    = 0
        self.insanity      = 0

        self.distance_travelling = 0
        self.actions_left  = 3

        self.traps_set     = False

    def display_stats(self, reverse=False, new_lines=[], reverse_filters=[], *filters):
        """ displays an entity's stats evaluating integers

            reverse: boolean
                reverse the way colors are displayed. 0 starts at green and increasing numeric value changes color

            new_lines: set (only numbers)
                places to insert new lines for ease of reading

            reverse_filters: set
                set only a couple of numeric attributes to be reversed

            filters: args
                numeric attributes to exclude
        """

        def print_spaces(base, text):
            spaces = ""
            for _ in range(base - len(text)):
                spaces += " "

            return spaces


        def evaluate(stat_name, stat, reverse):
            """ evaluates an integer returning a string with the integer colored either red, yellow, or green"""

            if stat_name in reverse_filters:
                reverse = not reverse

            if not stat:
                    print("─\n")
                    return

            # assign each stat a color based on how high it is
            if isinstance(stat, (int, float)):
                if (stat < 2 and not reverse) or (stat > 5 and reverse):
                    print(stat, "red")

                elif (stat < 5 and not reverse) or (stat > 2 and reverse):
                    print(stat, "yellow")

                else:
                    print(stat, "green")

            print("\n")


        attributes = self.ordered_attributes

        print("\n\nstats")
        print("\n───────────────\n")

        spaces = len(max(attributes.keys(), key=len)) + 3
        line = 0

        # display unfiltered attributes
        for category, info in attributes.items():
            if line in new_lines:
                print("\n")

            if category in filters:
                continue

            if isinstance(info, OrderedDict):
                print("\n~ " + category + "\n")

                for sub_category, sub_info in dict(info).items():
                    print("   ─ " + str(sub_category) + " : ")
                    evaluate(sub_category, sub_info, reverse)
            else:
                print(str(category) + print_spaces(spaces, category) + ": ")
                evaluate(category, info, reverse)

            line += 1

        print("\n───────────────\n")

    def check_debuff(self):
        """ ensures debuff attributes don't exceed certain levels without consequences """

        print("\neffects:\n")
        print("───────────────\n")
        debuff = False
        if self.exhaustion < 0:
          debuff = True
          print("your vision sharpens\n", "green")
          self.insanity += self.exhaustion

        if self.exhaustion > 10:
          debuff = True
          insanity = random.randint(self.exhaustion, self.exhaustion * 2)

          print("your vision swims\n", "yellow")

          self.insanity += insanity
          if self.exhaustion > 50:
            game.end(player)

        if self.starvation < 0:
          print("you feel full and satisfied\n", "green")
          self.exhaustion += self.starvation

        if self.starvation > 5:
              debuff = True
              exhaustion = random.randint(self.starvation, self.starvation * 2)
              damage = random.randint(self.starvation, self.starvation * 2)

              print("you feel almost nothing at all anymore\n", "red")

              self.exhaustion += exhaustion
              self.hp -= damage

        if self.exhaustion > 2:
            debuff = True
            self.starvation += round(self.exhaustion/4)
            print("you feel hollow\n", "yellow")

        if self.hp < 5:
          debuff = True
          print("you are missing an alarming amount of you\n", "yellow")

        if self.hp <= 0:
          game.end(self)

        if not debuff:
            print("none\n", "green")

    def camp(self, mainTrail):
        """ camping function """
        ui.set_print_speed(0)

        camping.view_stats(self)
        print("it is time to camp, as the night wears away.\n")
        print("what would you like to do?\n\n")
        print("W[Forward] /S[Back] /Enter[Done]\n")

        actions = ["sleep", "make fire", "find food", "wound care", "set traps", "commit suicide", "check map", "meditate"]

        random.shuffle(actions)

        padding = len(max(actions, key=len)) + 2 # for []
        self.actions_left = 3
        action = 0

        ui.set_print_speed(0)
        print("[{}]".format(actions[0])) # because nothing shows up originaly
        # action selection loop
        while self.actions_left > 0:
            if os.name == "nt":
                char = chr(ord(msvcrt.getch()))

                if ord(char) == 13:
                    char = "\n"
            else:
                char = getch.getch()

            if char.lower() == "w":
                action += 1
                if action > len(actions) - 1:
                    action = 0

                print("\r[{}]{}\r".format(actions[action], " " * padding))

            elif char.lower() == "s":
                action -= 1
                if action < 0:
                    action = len(actions) - 1

                print("\r[{}]{}\r".format(actions[action], " " * padding))

            elif char == "\n":
                ui.clr()
                ui.set_print_speed(0.05)
                decision = actions[action]
                print("selected [{}]\n".format(decision), "green")

                if decision == "sleep":
                    break

                self.actions_left -= 1
                print("[{}] actions remaining\n\n".format(self.actions_left))

                self.do(decision)
                action = 0

                ui.set_print_speed(0)
                print("\n\nselect new action:\n")
                print("[{}]".format(actions[0]))

            else:
                continue

        print("[begin sleep]\n")
        print("───────────────\n\n")

        attacked = False
        sleep = random.randint(1, 2) + (self.actions_left * 5)
        for _ in range(sleep):
            if random.randint(0, 100) > 10 and not self.traps_set:
                attacked = True

                event = game.get_event("night_events.txt")
                damage = random.randint(1, 2)
                print(event)
                print("    -{} hp\n".format(damage), "red")
                self.hp -= damage
                self.insanity += damage

                if self.hp <= 0:
                    game.end(self)

                time.sleep(.02)

        rest = random.randint(-2, 2) + sleep
        print("-{} exhaustion from sleep\n".format(rest), "green")
        self.exhaustion -= rest

        if not attacked:
            print("you find no evidence of attacks during the night.. yet..\n")

        self.check_debuff()

        input("\n\npress enter to continue...")

    def do(self, decision):
        """ executes a camping function """
        actions = {"make fire": camping.make_fire, "find food": camping.find_food, "wound care": camping.wound_care, "set traps": camping.set_traps, "commit suicide": camping.suicide, "check map": camping.check_map, "meditate": camping.meditate}
        action = actions[decision]
        action(self)

        if self.actions_left == 0:
            input("\npress enter to continue")

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self.ordered_attributes:
            self.ordered_attributes[key] = value

        if key not in self.ordered_attributes and key != "ordered_attributes":
            self.ordered_attributes.update({key: value})
