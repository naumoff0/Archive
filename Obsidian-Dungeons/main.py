""" main module """
import builtins
import codecs
import os
import sys

import colorama

sys.path.append(os.getcwd() + "/game")
import encounter
import game
import player_manager
import ui


def main():
    """ main menu """

    try:
        colorama.init()
        builtins.print = ui.delayed_print
        display_main_menu()

    finally:
        if game.WORLD_PATH:
            game.save(game.WORLD_PATH)


def display_main_menu():
    """ displays the main menu """

    main_menu = ui.Menu("Obsidian Dungeons")

    main_menu.add("Begin", player_manager.select)
    main_menu.add("New Player", player_manager.create)
    main_menu.add("Exit", sys.exit, 0)

    main_menu.display()


if __name__ == "__main__":
    main()
