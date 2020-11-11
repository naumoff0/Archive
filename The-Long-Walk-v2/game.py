""" game module """
import linecache
import random
import getch
import time
import sys
import os

import termcolor

import generation
import ui

MAP = generation.MainTrail()

def resource_path(relative_path):
    """sets resource path, does what it says on the tin"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def get_event(file):
    """ grabs a random line from a file """
    
    # change resource path based on os
    if os.name == "nt":
        path = resource_path("resources\\" + file)
    else:
        path = resource_path("resources/" + file)
        
    return linecache.getline(path, random.randint(1, sum(1 for line in open(path)))).strip()

def get_distance(player):
    """ visually displays how far the player is traveling. returns distance (int) """

    ui.set_print_speed(0.025)

    print("it is time to travel\n")
    print("what distance will you trek?\n\n")

    ui.set_print_speed(0)

    print("W[More] S[Less] Enter[Done]\n")

    distance = 0
    while True:
        if os.name == "nt":
            char = chr(ord(msvcrt.getch()))
            if ord(char) == 13:
                break
        else:
            char = getch.getch()

        # w is forward 1 mile, s is back. enter to exit
        if char.lower() == "w":
            distance += 1
        elif char.lower() == "s" and distance > 0:
            if distance == 1:
                continue

            distance -= 1
        elif char == "\n":
            break
        else:
            continue

        ui.remove_lines(1)
        print("traveling {} miles [".format(distance))
        print("·" * distance, "green")
        print("]\n")

        if distance >= 20 - player.exhaustion - player.starvation:
            ui.remove_lines(1)
            print("traveling {} miles [".format(distance))
            print("·" * distance, "green")
            print("]")
            print(" !! max distance !!\n", "red")
            distance -= 1

    player.distance_travelling = distance
    return player

def travel(player, trail):
    """allows for trail switching and throws up events and other things for the player to do"""
    distance = player.distance_travelling
    player.distance_travelling = 0
    ui.set_print_speed(0.1)
    print("\n[begin trek]\n")
    altTrails = trail.jackpoints


    ui.set_print_speed(0.02)
    print("───────────────\n\n")

    for _ in range(distance):
        player.distance_travelled += 1
        
        for subtrail in altTrails:
          if player.distance_travelled == subtrail.jackpoint and trail.currentJack == -1:
            ui.clr()
            print("passing the {} trail, mile marker {}\n".format(subtrail.jackname, subtrail.jackpoint), "yellow")
            print("take the {} trail?\n[y/n]".format(subtrail.jackname))
            decided = False
            while not decided:
              chc = input("> ")
              if chc in "yn":
                if chc == "y":
                  decided = True
                  break
                
                elif chc == "n":
                  decided = True
                  break
              
              else:
                ui.remove_lines(1)
            
            if chc == "y":
              trail.currentJack = subtrail.instance
            
            print("JACKED:{}\n".format(trail.currentJack))


        if random.randint(0, 100) + player.insanity > 95:
          dam = random.randint(1, 3)
          print("\n")
          ui.remove_lines(1)
          print(get_event("events.txt") + str(dam) + "\n", "red")
          player.hp -= dam
          player.insanity += dam
          if player.hp <= 0:
            end(player)

        else:
          if trail.currentJack == -1:
            tempname = "main trail"
          
          else:
            tempname = trail.jackpoints[trail.currentJack].jackname
          ui.set_print_speed(0)
          print("""
          << {} >>
          |  mile marker {}{}|""".format(tempname, player.distance_travelled, " " * (4 - len("{}".format(player.distance_travelled)) )))
          ui.remove_lines(2)
          ui.set_print_speed(0.025)
          time.sleep(.1)



    if trail.currentJack == -1:
      trail.player_position += distance

    else:
      trail.jackpoints[trail.currentJack].player_position += distance
      if trail.jackpoints[trail.currentJack].player_position >= trail.jackpoints[trail.currentJack].length:
        trail.player_position = trail.jackpoints[trail.currentJack].reentry
        print("you have finished the {} trail. the mile marker is {}.".format(trail.jackpoints[trail.currentJack].jackname, trail.player_position))
        trail.currentJack = -1

    player.starvation += round(distance / 5)
    exhst = round(distance / 2)

    try:
        player.exhaustion += random.randint(1, exhst)
        
    except ValueError:
        player.exhaustion += 0

    print("\n\n")
    player.check_debuff()
    return [player, trail]

def start(player):
    """ main game loop """
    
    MAP = get_map()
    trail = MAP
    distance = trail.length
    
    for _ in trail.jackpoints:
      print("{} : {} : {} >> {}\n".format(_.jackname, _.length, _.jackpoint, _.reentry))

    while player.hp > 0:
      player = get_distance(player)
      double = travel(player, trail)
      ui.update_insanity(player.insanity)
      player = double[0]
      trail = double[1]
      player.camp(trail)
      ui.update_insanity(player.insanity)

def end(player):
    """ end game message """
    generate_death_message()
    ui.update_insanity(0)
    print("\n\nyou made it {} miles before succumbing to the inevitable\n\n".format(player.distance_travelled), "yellow")
    sys.exit(0)

def win():
    """ win game message """
    print("\n\n!! you survived !!\n\n", "green")
    sys.exit(0)

def get_map():
  global MAP
  return MAP
    
def generate_death_message():
    """creates rng death message"""
    death = ["\n"]
    death.append(get_event("deathcauses.txt"))
    death.append(get_event("deathfiller.txt"))
    death.append(get_event("deathend.txt"))
    print("{} {} {} {}\n".format(death[0], death[1], death[2], death[3]), "red")