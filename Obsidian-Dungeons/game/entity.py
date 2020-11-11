""" entity class module """
import bisect
from collections import OrderedDict

import termcolor

import db_manager


class Entity(object):
    """ entity class """
    def __init__(self, name):
        self.ordered_attributes = OrderedDict()
        self.name = name

        self.xp = 1
        self.level = round(self.xp / 100) + 1

        self.equipment = OrderedDict()

    def display_stats(self, *filters):
        """ displays an entity's stats evaluating integers """
        attributes = self.ordered_attributes

        print("\n\nStats")
        print("\n───────────────\n")

        def evaluate(stat):
            """ evaluates an integer returning a string with the integer colored either red, yellow, or green"""
            if not stat:
                return "None"

            if isinstance(stat, (int, float)):
                if stat < 100:
                    stat = termcolor.colored(str(stat), "red")

                elif stat < 200:
                    stat = termcolor.colored(str(stat), "yellow")

                else:
                    stat = termcolor.colored(str(stat), "green")

            return stat


        for category, info in attributes.items():
            if category in filters:
                continue

            if isinstance(info, OrderedDict):
                print("\n~ " + category + "\n")

                for subcategory, sub_info in dict(info).items():
                    print("   ─ " + str(subcategory) + " : " + evaluate(sub_info) + "\n")

            else:
                print(str(category) + " : " + evaluate(info) + "\n")


        print("\n───────────────\n")

    def __setattr__(self, key, value):
        if key != "ordered_attributes":
            # if equipment is being added, add equipment durability with name
            if key == "equipment" and not isinstance(value, OrderedDict):
                result = db_manager.query("game/data.db", "items", "name", value.strip())

                if result:
                    self.equipment.update({value.strip(): result[0][9]})
                    self.ordered_attributes["equipment"] = self.equipment

                    return


        super().__setattr__(key, value)

        if key != "equipment":
            if key not in self.ordered_attributes and key != "ordered_attributes":
                self.ordered_attributes.update({key: value})


class Player(Entity):
    """ player class """
    def __init__(self, name):
        Entity.__init__(self, name)

        self.location = None
        self.description = OrderedDict.fromkeys(["faction", "type", "class"], 0)
        self.stats = OrderedDict.fromkeys(["health", "strength", "agility", "knowledge", "charisma", "wealth"], 0)


    def display_stats(self):
        Entity.display_stats(["location"])


class Npc(Entity):
    """ npc class """
    def __init__(self, name, alignment, attitude):
        Entity.__init__(self, name)

        self.alignment = alignment
        self.attitude = attitude

        self.description = OrderedDict.fromkeys(["info", "description", "faction"], None)
        self.stats = OrderedDict.fromkeys(["health"], 0)


    def display_stats(self, *filters):
        Entity.display_stats(filters)


    def determine_attitude(self):
        """ determines an npc's attitude """

        attitudes = OrderedDict({50: colored("hostile", "red"), 75: colored("unfriendly", "red"),
                                 100: colored("indifferent", "yellow"), 150: colored("friendly", "green"),
                                 200: colored("helpful", "green"), 300: colored("ally", "green")
                                })

        if self.attitude > 300:
            return colored("ally", "green") # bisect can't bisect left to something greater than 300 which doesn't exist

        keys = list(attitudes.keys())
        attitude = bisect.bisect_left(keys, self.attitude)

        return attitudes[keys[attitude]]


class Monster(Entity):
    """ monster class """
    def __init__(self, monster_type):
        Entity.__init__(self, monster_type)

        self.stats = OrderedDict.fromkeys(["health"], 0)
        self.power = None
        self.loot = None
