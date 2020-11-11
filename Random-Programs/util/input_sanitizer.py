import sys
import time

def accepted_inputs(acceptedInputs, choice):
    
    # repeat input until user gives valid data
    while choice not in acceptedInputs:
        print("-------------------------")    
        print("{} is not a valid option".format(choice))
        
        choice = input("Choice: ")
    
    return choice