class Player:
    
    def __init__(self, name, classType, weight, strength, endurance, agility, health):
        self.inventory = []
        self.name = name
        self.classType = classType
        self.weight = weight
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        
        self.health = health
        
    # add an item to players inventory
    def addItem(self, item):
        self.inventory.append(item) 
    
    # apply stats to player 
    def applyStats(self, weight, strength, endurance, agility):
        self.weight += int(weight)
        self.strength += int(strength)
        self.endurance += int(endurance)
        self.agility += int(agility)
        
    # return players an item in player's inventory
    def getItem(self, itemPlace):
        return self.inventory[itemPlace]
    
    # returns size of player's inventory
    def inventorySize(self):
        return len(self.inventory)

    def setHealth(self):
        self.health = (200 + self.strength + self.endurance + self.agility) - self.weight
        
    def displayHealth(self):
        print("{}'s Health: {}".format(self.name, self.health))
    
class Enemy:
    
    def __init__(self, name, size, power, armourClass, health):
        self.name = name
        self.size = size
        self.power = power
        self.armourClass = armourClass
        self.health = health
        
    def getHealth(self):
        return 10 * self.size
        
    def displayHealth(self):
        print("{}'s Health: {}".format(self.name, self.health))

    def setHealth(self):
        self.health = (self.size * 5) + (self.armourClass * 10) + self.power



class Item:
    
    def __init__(self, name, tier, weight, strengthAdr, enduranceAdr, agilityAdr):
        self.name = name
        self.tier = tier # 1, 2, 3, 4  (1 being the best)
        self.weight = weight # x amount of pounds
        self.strengthAdr = strengthAdr
        self.enduranceAdr = enduranceAdr
        self.agilityAdr = agilityAdr

        