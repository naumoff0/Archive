""" game module """

import os
import pickle
import random
import shutil
import sys

import file_manager
import main
import spawn
import ui

WORLD_PATH = None


def menu(name, player_class, player_type):
    """ game menu, not to be confused with main menu """

    game_menu = ui.Menu("Game Menu\nPlaying as: {} ({} {})".format(name, player_class.capitalize(), player_type.capitalize()))

    game_menu.add("New Game", new_world, name)
    game_menu.add("Resume", resume)
    game_menu.add("Back", main.display_main_menu)

    game_menu.display()


def start(world_name, path=None):
    """ starts the game """

    if path:
        unzipdir(path)

    world_pkl = world_name + "/world.pkl"
    player_pkl = world_name + "/player.pkl"

    world = unpickle_entity(world_pkl)[0]
    player = unpickle_entity(player_pkl)[0]

    player.location = random.sample(world.towns, 1)[0]

    # intro
    ui.clr()
    print("You awaken in a town called {}...\n".format(player.location.name), "yellow")
    print("{}\n".format(player.location.description))
    print("\nPopulation: {}\n".format(player.location.population))

    save(WORLD_PATH)


def resume():
    """ resumes a game """

    world_menu = ui.Menu("Select a World")
    worlds = file_manager.find(".zip")
    world_names = []

    for world in worlds:
        # remove everything but the world name
        world_name = world.replace("worlds", "").replace(os.getcwd(), "").replace("\\", "").replace("/", "").replace(".zip", "")

        world_menu.add(world_name)
        world_names.append(world_name)


    world_menu.display(False)

    if not worlds:
        print("\nNo worlds found \n")
        return

    options = list(range(1, len(worlds) + 1))
    choice = int(ui.accepted_input(*[str(s) for s in options]))

    global WORLD_PATH
    WORLD_PATH = worlds[choice - 1].replace(".zip", "")

    start(world_names[choice - 1], worlds[choice - 1]) # subtract 1 since menus start at 1


def new_world(player_name):
    """ creates a new world """

    while True:
        ui.clr()
        print("World name: ")
        world_name = input()

        if not world_name:
            print("\nInvalid world name!\n", "red")
            if not ui.prompt("Try again?", None):
                return

            continue

        path = "worlds/" + world_name.strip()

        if os.path.isdir(path) or os.path.isfile(path + ".zip"):
            if not ui.prompt("\nWorld already exists, want to overwrite it?", None):
                return

        file_manager.remove(path)
        os.makedirs(path)
        break


    print("\nGenerating World...", "green")
    world = spawn.world()

    pickle_entity(world, world_name, "world", "w")
    player = spawn.player(player_name)
    pickle_entity(player, world_name, "player", "w")

    global WORLD_PATH
    WORLD_PATH = path

    zipdir(path)
    start(world_name, path + ".zip")


def pickle_entity(instance, world_name, output_file, mode):
    """ pickles an instance or object and saves it to a .pkl file """

    with open("worlds/" + world_name + "/" + output_file + ".pkl", mode + "b") as pkl_file:
        pkl_file.write(pickle.dumps(instance))

    return


def unpickle_entity(path):
    """ unpickles objects from a file """

    unpickled_objects = []
    with open("worlds/" + path, "rb") as pkl_file:
        unpickled_objects.append(pickle.load(pkl_file))

    return unpickled_objects


def save(path):
    """ zips and retains cuurent state of a world """
    if os.path.exists(path):
        zipdir(path)


def zipdir(path):
    """ zips a directory. path can not end in .zip """

    shutil.make_archive(path, "zip", path)
    file_manager.remove(path)


def unzipdir(path):
    """ unzips a directory. path must end in .zip """

    shutil.unpack_archive(path, extract_dir=path.replace(".zip", ""))
    file_manager.remove(path)
