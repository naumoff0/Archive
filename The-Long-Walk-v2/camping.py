import random

import game
import ui

def make_fire(player):
    """ creates a fire reducing chance of nighttime attacks """
    labor = random.randint(5, 10)

    print("you gather wood and make a fire\nyou feel warm, and the night recedes\n")
    print("-{} exhaustion\n".format(labor), "yellow")

    player.exhaustion -= labor
    if random.randint(1, 4) <= 3:
      player.traps_set = True
    
    else:
      print("eyes scuttle about you, unafraid of the heat\n", "red")

def find_food(player):
    """ prevents starvation """
    labor = random.randint(5, 10)
    food = random.randint(5, 10)

    print("you forage for food\n")
    print("+{} exhaustion  ".format(labor), "red")
    print("+{} food\n".format(food), "green")

    player.exhaustion += labor
    player.starvation -= food

def wound_care(player):
    """ replenishes hp """
    labor = random.randint(1, 5)
    heal = random.randint(4, 9)

    print("rub mud on it - everything stops bleeding eventually\n")
    print("+{} exhaustion  ".format(labor), "red")
    print("+{} hp\n".format(heal), "green")

    player.exhaustion += labor
    player.hp += heal

def set_traps(player):
    """ reduces nocturnal attacks almost completely """
    labor = random.randint(5, 10)
    print("punji pits from 'nam find use in this black hell too\n")
    print("+{} exhaustion  \n".format(labor), "red")

    player.exhaustion += labor
    player.traps_set = True

def view_stats(player):
    """ shows player their statistics """
    player.display_stats(False, [1], ["exhaustion", "dehydration", "starvation", "distance_left", "insanity"], [], "actions_left", "distance_left", "night_attack_chance", "traps_set")

def suicide(player):
    """ kills player """
    player.insanity = 0
    ui.update_insanity(player.insanity)

    print("a tree appears a grand final resting place\n")
    player.insanity + 50
    ui.update_insanity(player.insanity)

    print("the noose is a comfortable perch.\n")
    player.insanity + 100
    ui.update_insanity(player.insanity)

    print("the light beckons to you, warm and inviting\n")
    player.insanity + 200
    ui.update_insanity(player.insanity)

    print("you stand a monument to your own failure.\n")
    game.end(player)

def check_map(player):
    """ does something with the cool trails """
    map = game.get_map()
    print("{} : {} miles to exit\n".format(map.name, map.length - player.distance_travelled))
    print("{} : {} miles, shows up around {}?\n".format(map.jack1.jackname, map.jack1.length, round(map.jack1.jackpoint, -1)))
    print("{} : {} miles, shows up around {}?\n".format(map.jack2.jackname, map.jack2.length, round(map.jack2.jackpoint, -1)))
    print("{} : {} miles, shows up around {}?\n".format(map.jack3.jackname, map.jack3.length, round(map.jack3.jackpoint, -1)))
    print("{} : {} miles, shows up around {}?\n".format(map.jack4.jackname, map.jack4.length, round(map.jack4.jackpoint, -1)))

def meditate(player):
    med_effect = random.randint(-20, 5)
    if med_effect > 0:
      print("you feel restless", "red")
      player.insanity += med_effect
    
    else:
      print("you feel calm", "green")
      player.insanity += med_effect

    return player



