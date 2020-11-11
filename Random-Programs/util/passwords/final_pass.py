from ui import *
import getch
        

def hide():
    password = ""
    while True:
        char = getch.getch()
        if char == "\n":
            break
        else:
            sys.stdout.write("*")
            sys.stdout.flush()
            password += char
    print("")
    return password
    
    
def createNewPassword():
    while True:
        printS("ENTER PASSWORD, PASSWORDS MUST MATCH\n", .02, 'red')
        printS("/>", .02)
        password = hide()
        passwordHash = hash(password)
        printS("/>", .02)
        password2 = hide()
        passwordHash2 = hash(password2)
        if passwordHash != passwordHash2:
            printS("ERROR... REENTER PASSWORD\n", .02, 'red')
        elif passwordHash == passwordHash2:
            printS("PASSWORD IS {}//HASH IS {}\n".format(password, passwordHash), .02)
            return password


def login(currentPassword):
    for i in range(3):
        currentPassword = hash(currentPassword)
        password = hash(hide())
        if password == currentPassword:
            breakup = list(str(password))
            breakup2 = list(str(currentPassword))
            for i in range(len(breakup)):
                printS(chr(8), .02)
                printS("VERIFYING[{}%]\r".format(round(float(100 * (i / len(breakup))), 2)), .002)
                time.sleep(0.5)
            printS("VERIFIED[100%]     \n", .02)
                
        elif password != currentPassword:
            printS("LOGIN FAILED WITH HASH DIFFERENCE OF {}\n".format(password - currentPassword), .02)
    printS("ACTUAL PASSWORD HASH TESTING ONLY {}\n".format(currentPassword), .02)
    