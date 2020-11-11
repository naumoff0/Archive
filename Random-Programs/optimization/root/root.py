""" square root finder """
import time
import random

def main():
    """ main module """
    n = 0
    x = int(input("Number: "))
    n = 1
    z = random.ldrandint(2, 20)
    while True:
        if round((z * z), 2) == round(x, 2):
            z = round(z, 4)
            p = z * z
            z = str(z)
            print(p)
            print(z.rstrip(z[:-4]))
            return
        elif round((z * z), 2) <= round(x, 2):
            z += round(((z * z)/10000), 4)
            print(z, end="\r")
            n += 1
            if n >= 1000:
                z += round(((z * z)/n), 2)
                if n >= 10000:
                    p = z * z
                    z = str(z)
                    print(p)
                    print(z.rstrip(z[:-4]))
                    return
            time.sleep(.001)
        elif round((z * z), 2) >= round(x, 2):
            z -= round(((z * z)/10000), 4)
            n += 1
            if n >= 1000:
                z -= round(((z * z)/n), 2)
                if n >= 10000:
                    p = z * z
                    z = str(z)
                    print(p)
                    print(z.rstrip(z[:-4]))
                    print(z, end="\r")
                    return
            time.sleep(.001)
if __name__ == "__main__":
    main()