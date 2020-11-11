""" encounter management module
    encounter options and descriptions must always be indented with 4 spaces

    + encounter description
    - encounter options
    :: separates commands
    {} = placeholder for any attribute to be printed

"""
import linecache
import random


class Encounter(object):
    """ encounter class """
    def __init__(self, description):
        self.description = description
        self.options = []

    def map_encounter(self, source, root, head):
        """ retrives options starting with -  root must be a line number """

        i = 1
        found = []
        while True:
            line = linecache.getline(source, root+i)
            if not line.strip() or line.startswith("+") or indentation(line) == indentation(linecache.getline(source, root)):
                break

            # checks if indentation is valid
            if indentation(line) == indentation(linecache.getline(source, root)) + 1:
                if head:
                    new_encounter = Encounter(line.strip())
                    found.append(new_encounter)
                    new_encounter.options = self.map_encounter(source, root+i, False)

                else:
                    new_option = Option(line[1:].split("::"))
                    found.append(new_option)
                    new_option.encounter = self.map_encounter(source, root+i, True)
            i += 1

        return found


class Option(object):
    """ option class """
    def __init__(self, description, commands=None):
        self.description = description
        self.commands = commands
        self.encounter = None


def indentation(line):
    """ returns the number of indents from a line. indents are 4 spaces long """
    return (len(line) - len(line.lstrip())) / 4


def random_encounter(source):
    """ generates a random encounter from a source file """

    while True:
        line_num = random.randint(1, sum(1 for line in source))
        description = linecache.getline(source, line_num)

        if description.startswith("+"):
            new = Encounter(description)
            new.options = new.map_encounter(source, line_num, False)
            break

    return new
