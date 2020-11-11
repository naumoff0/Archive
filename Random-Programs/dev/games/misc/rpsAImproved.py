import sys
from random import randint
#stable build 0.1
def main():
    
    # main menu
    print("Welcome to Rock-Paper-Scissors!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("0) Exit")
    print("1) Play Against Bot")
    choice = input(">> ")
    userInput(['1'], choice)
    
        # game loop
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("0 to exit")
        print("rock, paper, scissors, SH00T\n")
        choice = input(">> ")

        userInput(['rock', 'paper', 'scissors'], choice)

        botChoice = bot()
        print("Bot: {}".format(botChoice))
        print("You: {}".format(choice))
            
        if botChoice == "rock" and choice == "paper":
            print("You cover up a rock. Great")
        elif botChoice == "rock" and choice == "scissors":
            print("You lose... you absolute failure")
        elif botChoice == "scissors" and choice == "rock":
            print ("You smash some scissors, destroyer of worlds")
        elif botChoice == "scissors" and choice == "paper":
            print ("You lose... HA HA HA")
        elif botChoice == "paper" and choice == "rock":
            print("You lose... to paper.. WEAKLING")
        elif botChoice == "paper"  and choice == "scissors":
            print("You omnomed the paper with your scissors")
        else:
            print("No one wins...")
    
            
def bot():
    rollroll = randint(1, 3)
    
    if rollroll == 1:
        return "rock"
    elif rollroll == 2:
        return "paper"
    elif rollroll == 3:
        return "scissors"
    else:
        return "edamame"

# ensure user gives specified input
def userInput(acceptedInputs, choice):
        while choice not in acceptedInputs:
            if choice == '0':
                print("Exiting...")
                sys.exit(0)
            
            print("~~~~~~~~~~~~~~~~~~~~~~~~")    
            print("{} is not a valid option".format(choice))
            choice = input("Choice: ")


if __name__ == "__main__":
    main()
    
