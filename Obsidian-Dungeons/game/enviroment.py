""" contains all of the enviroment classes """

class Enviroment(object):
    """ base enviroment class """
    def __init__(self, name, description):
        self.name = name
        self.description = description


class World(Enviroment):
    """ world class. contains towns, castles, and dungeons"""
    def __init__(self, name, description):
        Enviroment.__init__(self, name, description)

        self.towns = None
        self.castles = None


class Town(Enviroment):
    """ town class. contains npcs """
    def __init__(self, name, population, description):
        Enviroment.__init__(self, name, description)

        self.population = population
        self.encounters = []


class Castle(Enviroment):
    """ castle class. contains dungeons and loot """
    def __init__(self, name, description):
        Enviroment.__init__(self, name, description)

        self.dungeons = None


class Dungeon(Enviroment):
    """ dungeon class """
    def __init__(self, name):
        Enviroment.__init__(self, name, "None")

        self.rooms = None


class Room(Enviroment):
    """ room class """
    def __init__(self, name, description):
        Enviroment.__init__(self, name, description)

        self.paths = None
        self.exits = None
        self.encounters = []
        #self.loot = None
        #self.monsters = None


class Encounter(object):
    """ encounter class """
    def __init__(self):
        self.description = None
        self.options = None
