import glob2
import subprocess
from uiaddons import cls


def main():
    cls()
    name = input("Name of file to run: ")
    
    subprocess.call(["python3 ", name], shell=True)
    cls()
    
    
if __name__ == "__main__":
    main()
    