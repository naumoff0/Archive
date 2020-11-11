import subprocess

# install dependencies
print("installing dependencies...")
subprocess.call(["pip3 install --user performance"], shell=True)
subprocess.call(["python3 -m pip install perf"], shell=True)

print("\n\n__________________________")
print("dependencies now satisfied")

import sys
import performance
from random import randint
from UIAddons import *
    
def main():
    # check if user has python 3
    if sys.version_info[0] < 3:
        print("please run with python3")
        sys.exit(1)
        
    cls()
    print("welcome to easy auto benchmarker")
    print("load program? (benchmark times will vary per enviroment)")
    print("[y/n]")
    chc = uInput(["y","Y","n","N"])
    if chc == "n" or chc == "N":
        sys.exit(0)
        
    subprocess.call(["python3 -m performance run --python=python3 -r -b all -o log.log"], shell=True)
    

        
if __name__ == "__main__":
    main()
    
