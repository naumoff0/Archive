import glob2
import sys
import os
import py2exe
from distutils.core import setup

sys.argv.append("py2exe")

def main():
    fileToExe = input("file to convert into executable: ")


def find_all_files():
    """ finds every .py file in all subdirectorys and their corresponding modules """
    directory = os.path.dirname(os.path.realpath(__file__))
    
    return glob2.glob(directory + "/**/*.py")
    
def toExe(file):
    print("converting to executable...")
    setup(
    options = {"py2exe": {"bundle_files": 1, "compressed": True}},
    windows = [{"script": "single.py"}],
    zipfile = None,
    )


if __name__ == "__main__":
    main()