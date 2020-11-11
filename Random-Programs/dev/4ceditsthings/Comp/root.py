""" square root birch """
import time
import random
#PROTECTED
def main():
    """ this program smex up numbie wumbies """
    n = 0
    x = int(input("Number: "))#Takes the number you want to square root
    z = random.randint(2, 4)#gets a random number

    while True:
        if round((z * z), 5) == round(x, 5):#If the number works print it and end
            z = round(z, 4)
            z = str(z)
            with open("file.txt", "w") as att_file:
                att_file.write(z+"\n")
            print(z.rstrip(z[:-4]))
            return

        elif round((z * z), 5) <= round(x, 5):#if its to small add a small amount
            z += .0001
            print(z, end="\r")
            n += 1
            time.sleep(.0001)

        elif round((z * z), 5) >= round(x, 5):#if its to big subtract small amount
            z -= .0001
            print(z, end="\r")
            n += 1
            time.sleep(.0001)


if __name__ == "__main__":
    main()
