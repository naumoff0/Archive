"""
ui testing
"""
import sys
import time
import random
import psutil

def print(text, end="\n"):
    """ print """
    for _ in text:
        sys.stdout.write(_)
        sys.stdout.flush()
        time.sleep(.02)

    sys.stdout.write(end)

def startup():
    mem = psutil.virtual_memory()
    usr = psutil.users()
    """ startup """
    print("starting terminal")
    print("memory test")

    for _ in mem:
        print(mem[_])


startup()
