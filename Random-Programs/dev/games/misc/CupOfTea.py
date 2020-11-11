import time


def main():
    print("Options for a making a Cup of Tea")
    print("Steep that tea!")
    print("DRINK IT")
    print("Buy some tea")
    print("Inspect element on tea")
    
    steep()

def steep():

    clr()
    
    for i in range(8):
        print("Boiling water")
        print("     _o_    :'")
        print(" ,-.'---`.__ ;")
        print("((j`=====',-'")
        print(" `-\     /")
        print("    `-=-'     ")
        time.sleep(0.5)
        clr() 
        
        print("Boiling water.")
        print("     _o_    :'")
        print(" ,-.'---`.__ ;")
        print("((j`=====',-'")
        print(" `-\     /")
        print("    `-=-'     ")
        
        time.sleep(0.5)
        clr()
        print("Boiling water..")
        print("     _o_    :'")
        print(" ,-.'---`.__ ;")
        print("((j`=====',-'")
        print(" `-\     /")
        print("    `-=-'     ")
        
        time.sleep(0.5)
        clr()          
        print("Boiling water...")
        print("     _o_    :'")
        print(" ,-.'---`.__ ;")
        print("((j`=====',-'")
        print(" `-\     /")
        print("    `-=-'     ")
        
        time.sleep(0.5)
        clr()         

def clr():
    # clearscreen
    print(chr(27) + "[2J")    
    
    
if __name__ == "__main__":
    main()