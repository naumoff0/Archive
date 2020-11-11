# Secure Containment Breach?
import subprocess
import os



def switch():
    """ git commit user changer """
    print("git commit switcher ready")
    human = input("moshi moshi? new committer\n> ").lower()

    if human == "cole":
        subprocess.call("git config --global user.email \"cole.leckey.22@gmail.com\"", shell=True)

    elif human == "peter":
        subprocess.call("git config --global user.email \"peter.naumoff1@gmail.com\"", shell=True)

    elif human == "alaric":
        subprocess.call("git config --global user.email \"alaricshaw@gmail.com\"", shell=True)

    else:
        print("whomst'v'ed let u out of ur cage?")
        return

    print("commit user switched to {}".format(human))

def commit():
    os.chdir("/home/ubuntu/workspace")
    switch()
    """
    print("Message")
    message = input("> ")
    print("Target Dir")
    directory  = input("> ")
    os.chdir("/home/ubuntu/workspace/" + directory)
    subprocess.call("git add .", shell = True)
    subprocess.call("git commit -m \"{}\"".format(message), shell=True)
    subprocess.call("git push -f", shell=True)
    print("Finished.")
    """

if __name__ == "__main__":
    commit()