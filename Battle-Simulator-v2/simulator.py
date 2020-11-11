import time
import linecache
from ui_helpers import clearScreen
from random import randint
from entity_initializer import instanceLoader
from entity_initializer import itemCheck


# dice roll function
def rollDice(low, high):
    diceRoll = randint(low, high)
    return diceRoll
 

def battle(option, contestant1, contestant2):
    
    clearScreen() 
    
    print("Welcome to the arena!\n")
    print("Starting Contestants and their Stats:\n")


    if option == "player":
        
        # initialize two player instances 
        player1 = instanceLoader("player", contestant1)
        player2 = instanceLoader("player", contestant2)
        
        player1.displayHealth()
        player2.displayHealth()
        
        # effectiveness is calculated by adding all players stats together excluding weight & health
        print("{}'s Overall Effectiveness: {}%".format(player1.name, player1.strength + player1.endurance + player1.agility))
        print("{}'s Overall Effectiveness: {}%\n\n".format(player2.name, player2.strength + player2.endurance + player2.agility))

        print("{}'s Bet: High".format(player1.name))
        print("{}'s Bet: Low\n".format(player2.name))
        
        player1Start = False
        player2Start = False
            
        # keep rolling dice until one player wins bet
        while True:    
            
            if rollDice(-100, 100) > 0:
                print("Dice roll is high!")
                player1Start = True
                break
            
            elif rollDice(-100, 100) < 0:
                print("Dice roll is low!")
                player2Start = True
                break
            
            else:
                continue
            
        input("Press enter to begin battle...")
        
        beginBattle(2)
        
        # game loop
        while True:
            
            if player1Start == True:

                # player 1 hits, player 2 blocks
                hit = playerHit(player1)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player2)
                    
                if block < hit:
                    player2.health = player2.health - (hit - block)
                
                player1.displayHealth()
                player2.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()   
                
                # ensure players are still alive
                if entityDead(player1, player2, 3) or entityDead(player2, player1, 3):
                    break 
                    
                # player 2 hits, player 1 blocks
                hit = playerHit(player2)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player1)
                    
                if block < hit:
                    player1.health = player1.health - (hit - block)
                
                player1.displayHealth()
                player2.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()   
                
                # ensure players are still alive
                if entityDead(player1, player2, 3) or entityDead(player2, player1, 3):
                    break 
                        
            else:
                # player 2 hits, player 1 blocks
                hit = playerHit(player2)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player1)
                    
                if block < hit:
                    player1.health = player1.health - (hit - block)
                
                player1.displayHealth()
                player2.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()   
                
                # ensure players are still alive
                if entityDead(player1, player2, 3) or entityDead(player2, player1, 3):
                    break     
                    
                # player 1 hits, player 2 blocks
                hit = playerHit(player1)   

                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player2)
                    
                if block < hit:
                    player2.health = player2.health - (hit - block)
                
                player1.displayHealth()
                player2.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()   
                
                # ensure players are still alive
                if entityDead(player1, player2, 3) or entityDead(player2, player1, 3):
                    break 
                    
      
        input("Press enter to continue...")
        
    elif option == "enemy":
        enemy = instanceLoader("enemy", contestant1)
        player = instanceLoader("player", contestant2)
        
        enemy.displayHealth()
        player.displayHealth()
        
        # effectiveness is calculated by adding all players stats together excluding weight & health
        print("{}'s Overall Effectiveness: {}%".format(enemy.name, enemy.size + enemy.power + (enemy.armourClass * 5)))
        print("{}'s Overall Effectiveness: {}%\n\n".format(player.name, player.strength + player.endurance + player.agility))

        print("{}'s Bet: High".format(enemy.name))
        print("{}'s Bet: Low\n".format(player.name))
        
        enemyStart = False
        playerStart = False
            
        # keep rolling dice until one player wins bet
        while True:    
            
            if rollDice(-100, 100) > 0:
                print("Dice roll is high!")
                enemyStart = True
                break
            
            elif rollDice(-100, 100) < 0:
                print("Dice roll is low!")
                playerStart = True
                break
            
            else:
                continue
        input("Press enter to begin battle...")
        
        beginBattle(2)
        
        # game loop
        while True:
            
            if enemyStart == True:
                # enemy hits, player blocks
                hit = enemyHit(enemy)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player)
                
                if block < hit:
                    player.health = player.health - (hit - block)       
                    
                enemy.displayHealth()
                player.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()     

                # ensure players are still alive
                if entityDead(player, enemy, 3) or entityDead(enemy, player, 3):
                    break 
                    
                # player hits, enemy blocks
                hit = playerHit(player)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = enemyBlock(enemy)
                
                if block < hit:
                    enemy.health = enemy.health - (hit - block)   
                    
                enemy.displayHealth()
                player.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()     
                
                # ensure players are still alive
                if entityDead(enemy, player, 3) or entityDead(player, enemy, 3):
                    break 
                        
            else:
                # player hits, enemy blocks
                hit = playerHit(player)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = enemyBlock(enemy)
                
                if block < hit:
                    player1.health = player1.health - (hit - block) 
                    
                enemy.displayHealth()
                player.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen()
                    
                # ensure players are still alive
                if entityDead(enemy, player, 3) or entityDead(player, enemy, 3):
                    break     
            
                # enemy hits, player blocks
                hit = enemyHit(enemy)   
                input("Press enter to continue...")
    
                clearScreen()   
    
                block = playerBlock(player)
                
                if block < hit:
                    player.health = player.health - (hit - block)       
                    
                enemy.displayHealth()
                player.displayHealth()
                
                input("Press enter to continue...")
    
                clearScreen() 
                
                # ensure players are still alive
                if entityDead(enemy, player, 3) or entityDead(player, enemy, 3):
                    break  
                    
      
        input("\nPress enter to continue...")
        
    else:
        print("Fix function parameters.")
        return False

    
def playerHit(player):
    
    mainWeapon = "hands"
    weaponStrength = 0
    
    for item in range(player.inventorySize()):
        # initialize a new item
        currentItem = instanceLoader("item", player.getItem(item))
        
        # if item is in a valid weapon file and it's strength is better than previous weapon
        if itemCheck(player.getItem(item), "LOCATION") != "items/clothing.csv" and int(currentItem.strengthAdr) > weaponStrength:
            # set current strongest weapon to be the main weapon
            weaponStrength = int(currentItem.strengthAdr)
            mainWeapon = currentItem.name
    
    # choose a random line to select an action from
    action = linecache.getline("entity_data/actions.txt", rollDice(1, sum(1 for action in open("entity_data/actions.txt")))).rstrip('\n')

    # mega sword of epicness        
    print("              (O)")
    print("              <X|")
    print("   o          <X|")
    print("  /| ......  /:X\------------------------------------------------,,,,,,")
    print("(O)[]XXXXXX[]X:X+}=====<{ATTACK!}>=========================------------>")
    print("  \| ^^^^^^  \:X/------------------------------------------------''''''")
    print("   o          <X|")
    print("              <X|")
    print("              (O)\n")
    
    effectiveness = rollDice(1, 200)  
    hit = round(weaponStrength * (effectiveness * 0.1))
    
    print("{} {}s at his opponent with a {}! Hit is {}% Effective dealing {} damage!\n".format(player.name, action, mainWeapon, effectiveness, hit))
    
    return hit


def playerBlock(player):
    
    armour = "bare skin"
    bestItemStrength = 0
    currentItemStrength = 0
    
    for item in range(player.inventorySize()):
        # initialize a new item
        currentItem = instanceLoader("item", player.getItem(item))
        
        currentItemStrength = int(currentItem.strengthAdr) + int(currentItem.agilityAdr) + int(currentItem.enduranceAdr)
        
        # if item is in clothing file and it's effectiveness is better than previous item
        if itemCheck(player.getItem(item), "LOCATION") == "items/clothing.csv" and currentItemStrength > bestItemStrength:
            # set current strongest weapon to be the main weapon
            bestItemStrength = currentItemStrength
            armour = currentItem.name
            
            
    # almighty sheild of nobble! legendary ability to fend off wild Coles        
    print("   |\                     /)")
    print(" /\_\\\\__               (_//")
    print("|   `>\-`     _._       //`)")
    print(" \ /` \\\\  _.-`:::`-._  //")
    print("  `    \|`    :D:    `|/")
    print("        |     :E:     |")
    print("        |.....:F:.....|")
    print("        |::::::E::::::|")
    print("        |     :N:     |")
    print("        \     :D:     /")
    print("         \    :::    /")
    print("          `-. ::: .-'")
    print("           //`:::`\\\\")
    print("          //   '   \\\\")
    print("         |/         \\\\ \n")
    
    effectiveness = rollDice(1, 100)
    block = round(bestItemStrength * (effectiveness * 0.05))
    
    print("{}'s {} absorbs impact with {}% effectiveness blocking {} damage!\n".format(player.name, armour, effectiveness, block))
    
    return block
    

def enemyHit(enemy):
    
    print("         />")
    print("        /<")
    print("\\\\\\\\\\\\(O):::<======================================-")
    print("        \<")
    print("         \>")
    
    # choose a random line to select an action from
    action = linecache.getline("entity_data/actions.txt", rollDice(1, sum(1 for action in open("entity_data/actions.txt")))).rstrip('\n')
    
    effectiveness = rollDice(1, 200)  
    hit = round(enemy.power * (effectiveness * 0.02))
    
    print("{} {}s at his opponent! Hit is {}% Effective dealing {} damage!\n".format(enemy.name, action, effectiveness, hit))
    
    return hit    
    
def enemyBlock(enemy):
    print("  |`-._/\_.-`|")
    print("  |    ||    |")
    print("  |___o()o___|")
    print("  |__((<>))__|")
    print("  \   o\/o   /")
    print("   \   ||   /")
    print("    \  ||  /")
    print("     '.||.'")
    print("       ``")

    effectiveness = rollDice(1, 100)
    block = round((enemy.armourClass * 10) * (effectiveness * 0.02))
    
    print("{} absorbs impact with {}% effectiveness blocking {} damage!\n".format(enemy.name, effectiveness, block))
    
    return block
    

def beginBattle(delay):
    
    clearScreen() 
        
    # BEGIN BATTLE!!!!        
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
    print("########  ########  ######   #### ##    ##       ########     ###    ######## ######## ##       ######## ")
    print("##     ## ##       ##    ##   ##  ###   ##       ##     ##   ## ##      ##       ##    ##       ##       ")
    print("##     ## ##       ##         ##  ####  ##       ##     ##  ##   ##     ##       ##    ##       ##       ")
    print("########  ######   ##   ####  ##  ## ## ##       ########  ##     ##    ##       ##    ##       ######   ")
    print("##     ## ##       ##    ##   ##  ##  ####       ##     ## #########    ##       ##    ##       ##       ")
    print("##     ## ##       ##    ##   ##  ##   ###       ##     ## ##     ##    ##       ##    ##       ##       ")
    print("########  ########  ######   #### ##    ##       ########  ##     ##    ##       ##    ######## ######## ")
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->")
        
    time.sleep(delay)
    clearScreen()



# check if player has positive health
def entityDead(entity1, entity2, delay):
    
    if entity1.health <= 0:
        
        clearScreen()
        
        print("{} WINS!!!".format(entity2.name))
        print("{} dies in the least epic way possible\n".format(entity1.name))
        
        entity1.displayHealth()
        entity2.displayHealth()
        
        time.sleep(delay)
        
        return True
        
    return False
    

# TODO create battle log
# TODO implement special abilities with conditons
# TODO name conflict prevention for adding anything
# TODO create item profile for each player
# TODO create file writing function (low priority)
# TODO add prestige bonuses for players that have won more battles