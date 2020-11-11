import os
import sys
import csv
from entity import Player
from entity import Enemy
from entity import Item


# loads instances of players, enemys, or items into memory
def instanceLoader(entityType, entityName):

    if entityType == "item":
        
        # check if item exists
        if itemCheck(entityName, "FOUND"):
            
            # open file where item is located
            with open(itemCheck(entityName, "LOCATION"), "r") as file:
                reader = csv.reader(file, delimiter=',')
                
                # search each row to find item
                for row in reader:
                    if row[0] == entityName:
                        # create, initialize, and return the item found
                        item = Item(entityName, row[1], row[2], row[3], row[4], row[5])
                        return item
        else:
            print("{} does not exist".format(entityName))
            sys.exit(2)
                    
    # ensure csv file exists
    if os.path.isfile("entity_data/" + entityType + ".csv" == False):
        print("{} data does not exist. Please restart and create a new {} data file.".format(entityType.capitalize(), entityType.capitalize()))
        sys.exit(3)    
    
    with open("entity_data/" + entityType + ".csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        # search every first value until name is found
        for name in reader:
            if entityName == name[0]:
                # create a new entity with values found in csv file
                if entityType == "player":
                    # intialize a player with default values
                    # Class: Human, Weight: 100lbs Strength: 10, Endurance: 20, Agility: 20 Health: 0 (given a value based on other values)
                    player = Player(entityName, "Human", 100, 10, 20, 20, 0)
                    
                    # open up class types file and search for player's class
                    with open("entity_data/class_types.csv", "r") as classTypeFile:
                        classReader = csv.reader(classTypeFile, delimiter=',')

                        for row in classReader:
                            # if class type (row[0]) is equal to player's class type (name[1])
                            if row[0] == name[1]:
                                player.classType = row[0]
                                # add items to players inventory
                                for item in row:
                                    if item != name[1] and itemCheck(item, "FOUND"):
                                        player.addItem(item)


                    # find item and apply it's stats to player
                    for item in range(player.inventorySize()):

                        # make sure item stored in inventory still exists
                        if itemCheck(player.getItem(item), "FOUND") == False:
                            print("Item in inventory does not exist anymore")
                            return False
                            
                        itemDirectory = itemCheck(player.getItem(item), "LOCATION")
                        
                        # open file where item is stored
                        with open(itemDirectory, "r") as itemFile:
                            itemReader = csv.reader(itemFile, delimiter=',')

                            # search for item name in the first string of every row
                            for row in itemReader:
                                
                                if row[0] == player.getItem(item):
                                    # apply the rest of items stats that can be applied to player (weight, strength, endurance etc...)
                                    player.applyStats(row[2], row[3], row[4], row[5])
                                    break
                            break
                        
                    # initialize player's health    
                    player.setHealth()
                    
                    # return initialized player
                    return player
                        
                elif entityType == "enemy":
                    with open("entity_data/enemy.csv") as file:
                        reader = csv.reader(file, delimiter=',')
                        
                        for row in reader:
                            if row[0] == entityName:
                                # intialize an enemy with values found in row
                                enemy = Enemy(entityName, int(row[1]), int(row[2]), int(row[3]), 0)
                                break
                            
                    # initialize enemy health
                    enemy.setHealth()
                    
                    # return initialized enemy
                    return enemy
                       
                else:
                    print("Entity type specified does not exist.")
    return False
    
    
def itemCheck(item, returnOption):

    if searchFile("items/clothing.csv", item, returnOption):
        return searchFile("items/clothing.csv", item, returnOption)
        
    elif searchFile("items/magic.csv", item, returnOption):
        return searchFile("items/magic.csv", item, returnOption)
        
    elif searchFile("items/melee.csv", item, returnOption):
        return searchFile("items/melee.csv", item, returnOption)
        
    elif searchFile("items/ranged.csv", item, returnOption):
        return searchFile("items/ranged.csv", item, returnOption)
        
        
# search files for a target value
def searchFile(directory, target, returnOption):
    # open file in specified mode
    with open(directory, "r") as file:
        reader = csv.reader(file)
        
        # search file row by row
        for row in reader:
            if row[0] == target:
                if returnOption == "LOCATION":
                    return directory
                elif returnOption == "FOUND":
                    return True
                else:
                    print("invalid function parameter")
                    
    return False
    