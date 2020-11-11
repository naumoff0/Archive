""" square root birch """
import time
import random

def main():
    """ this program sexes up numbie wumbies """

    x = int(input("Number: "))#Takes the number you want to square root
    y = int(input("To which Number: "))#And to which power you want the root to be
    z = random.randint(5, 10)#gets a random number

    while True:
        if round((z ** y), 5) == round(x, 5):#If the number works print it and end
            z = round(z, 4)
            z = str(z)
            print(z.rstrip(z[:-4]))
            return

        elif round((z ** y), 5) <= round(x, 5):#if its to small add a small amount
            z += .0001
            print(z, end="\r")

        elif round((z ** y), 5) >= round(x, 5):#if its to big subtract small amount
            z -= .0001
            print(z, end="\r")
            time.sleep(.001)


if __name__ == "__main__":
    main()
