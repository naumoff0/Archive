""" player management module """
import os
import sys

import db_manager
import game
import ui


def select():
    """ displays all players """

    ui.clr()

    all_players = db_manager.query("game/data.db", "players")
    if not all_players:
        print("\nNo players found.\n")
        return

    player_menu = ui.Menu("Select a player")

    for player in all_players:
        player_class = player[2].capitalize()
        player_type = player[1].capitalize()
        player_name = player[0]

        spaces = 40 - (len(player_class) + len(player_type) + len(player_name))
        combined = player_name + (" "*spaces)

        combined = combined + "({} {})".format(player_type, player_class)
        player_menu.add(combined)


    player_menu.display(False)
    print("\n000) Delete a Player\n")

    players = list(range(1, len(all_players) + 1))
    players = [str(p) for p in players]
    players.append("000") # delete player option

    choice = ui.accepted_input(*players)

    if choice == "000":
        del players[-1]
        ui.remove_lines(2)

        print("\nPlayer to delete: ", "red")
        choice = ui.accepted_input(*players)

        if ui.prompt("\nAre you sure?", None):
            # -1 because menu starts at 1
            db_manager.execute("game/data.db", "DELETE FROM players WHERE name = '{}';".format(all_players[int(choice) - 1][0]))
            print("\nPlayer has been deleted\n", "green")

        return

    selected_player = all_players[int(choice)-1]
    game.menu(selected_player[0], selected_player[1], selected_player[2])

    return


def create():
    """ character creation function """

    ui.clr()
    print("Create a New Player\n")
    print("--------------------\n")

    # ask for name
    while True:
        print("Name: ")
        name = input()
        name = name.strip()

        result = db_manager.query("game/data.db", "players", "name", name)
        if result or not name:
            print("\nName taken or too short/long\n", "red")
            ui.prompt("Try Again?", create)

            return

        break

    # display all player types
    type_menu = ui.Menu("Select a Type")
    player_types = db_manager.query("game/data.db", "types")

    for player_type in player_types:
        type_menu.add(player_type[0].capitalize())

    type_menu.display(False)
    type_chosen = ui.accepted_input(*list(range(1, len(player_types) + 1)))

    # display all player classes
    class_menu = ui.Menu("Select a Class")
    player_classes = db_manager.query("game/data.db", "classes")

    for player_class in player_classes:
        class_menu.add(player_class[0].capitalize())

    class_menu.display(False)
    class_chosen = ui.accepted_input(*list(range(1, len(player_classes) + 1)))

    type_chosen = player_types[int(type_chosen) - 1]
    class_chosen = player_classes[int(class_chosen) - 1]

    db_manager.add("game/data.db", "players", "name, type, class", name, type_chosen[0], class_chosen[0])
    print("\nPlayer has been created\n", "green")

    return
