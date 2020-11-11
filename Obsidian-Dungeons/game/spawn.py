""" spawns player and npc objects """

import os
import random
import re
import secrets
import sys

import db_manager
import entity
import enviroment
import file_manager


def player(name):
    """ returns a player object """

    account = db_manager.query("game/data.db", "players", "name", name)
    if not account:
        raise Exception("Player does not exist")

    # account is a single tuple within a list
    account = account[0]

    player_type = db_manager.query("game/data.db", "types", "name", account[1])
    player_class = db_manager.query("game/data.db", "classes", "name", account[2])

    player_type = player_type[0]
    player_class = player_class[0]

    new = entity.Player(name)

    # see tables.txt
    new.description["type"] = player_type[0]
    new.description["class"] = player_class[0]

    new.stats["health"] = player_type[2] + player_class[1]
    new.stats["strength"] = player_type[3] + player_class[2]
    new.stats["agility"] = player_type[4] + player_class[3]
    new.stats["knowledge"] = player_type[5] + player_class[4]
    new.stats["charisma"] = player_type[6] + player_class[5]
    new.stats["wealth"] = player_type[7] + player_class[6]

    equipment = player_type[1]

    for item in equipment.split(","):
        # setattr in entity inserts item into inventory
        new.equipment = item

    return new


def npc():
    """ returns an npc object """

    description = random_description("npc.txt", 3)

    new = entity.Npc(description[0], description[2], random.randint(25, 200))

    new.description["info"] = description[1]
    new.description["description"] = description[3]

    new.stats["health"] = random.randint(100, 500)
    print(str(new.stats) + "\n")

    items = db_manager.query("game/data.db", "items")
    amount = random.randint(1, len(items))
    equipment = list()

    for _ in range(amount):
        item = secrets.choice(items)
        if item not in equipment:
            equipment.append(item[0])
            continue

        # if item is already in list
        amount += 1


    for item in equipment:
        new.equipment = item

    return new


def monster(amount):
    """ returns a monster object """

    name = file_manager.retrive("monsters.txt", "RANDOM")
    monsters = []
    for _ in range(amount):
        new = entity.Monster(name)

        new.stats["health"] = random.randint(30, 250)
        new.xp = random.randint(100, 500)
        new.power = random.randint(40, 75)
        #new.loot = None

        # 1% chance there will be a mini-boss
        if random.randint(1, 100) == 1:
            new.stats["health"] = random.randint(300, 700)
            new.xp = random.randint(1000, 5000)
            new.power = random.randint(100, 150)
            #new.loot = None

            amount = 0 # stops multiple mini bosses from being spawned4

        monsters.append(new)

    return monsters


def world():
    """ returns a world object """

    description = random_description("worlds.txt", 1)
    new = enviroment.World(description[0], description[1])

    new.towns = town(random.randint(2, 5))
    new.castles = castle(random.randint(10, 15))

    return new


def town(amount):
    """ returns a list of town objects """

    descriptions = []
    towns = []
    for _ in range(amount):
        description = random_description("towns.txt", 2, descriptions, amount)

        new = enviroment.Town(description[0], description[1], description[2])
        new.encounters = random_encounters(new, "town_encounters.txt", random.randint(10, 30))

        towns.append(new)
        descriptions.append(description)

    return towns


def castle(amount):
    """ returns a list of castle objects """

    castles = []
    descriptions = []
    for _ in range(amount):
        description = random_description("castles.txt", 1, descriptions, amount)

        new = enviroment.Castle(description[0], description[1])
        new.dungeons = dungeon(random.randint(1, 3))

        castles.append(new)
        descriptions.append(description)

    return castles


def dungeon(amount):
    """ returns a list of dungeon objects """

    dungeons = []
    names = []
    for _ in range(amount):
        name = random_description("dungeons.txt", 0, names, amount)

        new = enviroment.Dungeon(name[0])
        new.rooms = room(random.randint(5, 10), 0)

        dungeons.append(new)
        names.append(name)

    return dungeons


def room(amount, depth):
    """ returns a list of room objects """

    max_depth = 3 # increase and expect exponential performance issues
    if depth >= max_depth:
        return

    rooms = []
    descriptions = []
    for _ in range(amount):
        description = random_description("rooms.txt", 1, descriptions, amount)

        new = enviroment.Room(description[0], description[1])
        new.encounters = random_encounters(new, "room_encounters.txt", random.randint(0, 3))
        new.paths = room(random.randint(0, 3), depth+1)

        # 20% chance next room will be an exit from the dungeon
        if random.randint(1, 100) <= 20 and new.paths:
            new.exits = random.sample(new.paths, 1)

        rooms.append(new)
        descriptions.append(description)

    return rooms


def random_description(source, end, descriptions=None, amount=None):
    """ returns a random description from source """

    description = file_manager.retrive(source, "RANDOM")
    description = "".join(description)
    new = ""

    # insert periods and commas when appropriate
    for index, char in enumerate(description):
        if not index + 2 > len(description) - 1:
            if char == "." or char == "," or char == "~":
                # +2 to skip over space. ~ is used to seperate numbers
                if description[index + 2].isupper() or char == "~":
                    new += "."
                else:
                    new += ","

                continue

        new += char

    # split the string by periods
    description = re.split("[.]", new)

    # joins the end of description together
    if len(description) > 1:
        description[end:len(description)] = [".".join(description[end:len(description)])]


    # strip whitespace
    description = [item.strip() for item in description]

    if descriptions and amount:
        # ensure description does not already exist in descriptions
        if description in descriptions:
            if amount == sum(1 for line in open(*file_manager.find(source))):
                return

            return random_description(source, end, descriptions, amount)

    return description


def random_encounters(instance, source, amount):
    """ returns random encounters from a source file """

    size = sum(1 for line in open(*file_manager.find(source)))
    if amount >= size:
        amount = size

    encounters = []
    for _ in range(amount):
        encounter = file_manager.retrive(source, "RANDOM")

        if encounter not in instance.encounters:
            encounters.append(encounter)
            continue

        amount += 1

    return encounters
