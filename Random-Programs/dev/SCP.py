# Secure Containment Breach
import subprocess


def switch(): #for imports
    """ git commit user changer """
    print("init git commit changer tool")
    human = input("moshi moshi?\n>> ").lower() # leave it at this pls

    if human == "cole":
        subprocess.call("git config --global user.email \"cole.leckey.22@gmail.com\"", shell=True)

    elif human == "peter":
        subprocess.call("git config --global user.email \"peter.naumoff@yahoo.com\"", shell=True)

    else:
        print("go back to your cage alaric ur a weeb lol git a github account")
        return "whomst'v'ed let him out of his cage?"


    print("done. (hopefully)")
    return


if __name__ == "__main__":
    switch()