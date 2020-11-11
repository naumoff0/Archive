# -*- coding: utf8 -*-
import builtins
import random
import os

import entity
import game
import ui


def main():
    """general setup and system checks"""
    builtins.print = ui.delayed_print

    if os.name == "nt":
        colorama.init()

    player = entity.Player()

    # exit the application when game.end() throws SystemExit exception
    try:

        game.start(player)

    except SystemExit:
        input("press enter to exit...")
        return


if __name__ == "__main__":
    main()
