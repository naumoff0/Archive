import sys

def menu():
    
    print("Menu:")
    print("1) Battle a fellow adventurer")
    print("2) Battle against an enemy")
    print("3) Add a player, enemy, or item")
    print("0) Exit")

    return

def getUserInput(acceptedInputs, choice):
    
    while choice not in acceptedInputs:
        if choice == '0':
            print("Exiting...")
            sys.exit(0)
            
        print("-------------------------")    
        print("{} is not a valid option".format(choice))

        choice = input("Choice: ")
    
    return choice
  
    
def clearScreen():
    # clearscreen
    print(chr(27) + "[2J")       