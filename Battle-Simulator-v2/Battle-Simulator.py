import sys
from entity_maker import makeEntity
from entity_maker import makeItem
from ui_helpers import clearScreen
from ui_helpers import menu
from ui_helpers import getUserInput
from simulator import battle
from entity_initializer import searchFile


def main():

    # check if user has python 3
    if sys.version_info[0] < 3:
        print("You must have python 3 installed!")
        print("If you have python 3 installed, try running with: python3 Exurrb-Battle-Simulator.py if your using the command line")
        sys.exit(1)
      
    while True:
        
        
        clearScreen()  
        
        menu()
        option = input("Choice: ")  
        
        option = getUserInput(['1', '2', '3'], option)    
        
        if option == '1':
            print("-------------------------")
            player1 = input("Player 1's Name: ")
            player2 = input("Player 2's Name: ")
            
            if(searchFile("entity_data/player.csv", player1, "FOUND") and searchFile("entity_data/player.csv", player2, "FOUND")):
                battle("player", player1, player2)
            else:
                print("-------------------------")
                print("Player does not exist!")
                input("Press enter to continue...")
                
        elif option == '2':
            print("-------------------------")
            enemy = input("Enemy Name: ")
            player = input("Player Name: ")
            
            if(searchFile("entity_data/enemy.csv", enemy, "FOUND") and searchFile("entity_data/player.csv", player, "FOUND")):
                battle("enemy", enemy, player)
            else:
                print("-------------------------")
                print("Entity does not exist!")
                input("Press enter to continue...")
        
        else:
            
            clearScreen() 
    
            print("Choose and option below:")
            print("1) Create new Enemy or Player")
            print("2) Create new Item")
            print("0) Exit")
            
            choice = input("Choice: ")
    
            choice = getUserInput(['1', '2'], choice)
            
            if choice == '1':
                makeEntity()
            else:
                makeItem()
    sys.exit(0)
            
    
    
if __name__ == "__main__":
    main()
