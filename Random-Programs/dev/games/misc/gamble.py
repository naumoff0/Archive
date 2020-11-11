def main():
    print("Welcome to the casino!")
    print("Rules are simple, guess a number, if you get it right you win 100000 dollars~")
    print("Else you loose 5 dollars")
    
    while True:
        try:
            number = int(input("Choose a number: "))
        except ValueError:
            print("INVALID NUMBER!!!")
        else:
            break

    if chooseNum(number) == number:
        while True:
            print("NOT POSSIVLE!!!!")
    else:
        print("You loose!")
    

def chooseNum(num):
    return num + 1
    
if __name__ == "__main__":
    main()