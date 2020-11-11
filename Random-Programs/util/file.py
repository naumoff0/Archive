import subprocess
import os


def findFiles(extensionFilter=None, toFile=None):
    # find directory
    path = os.getcwd()

    dirList = []
    for root, dirs, files in os.walk(path):
        # filter out hidden files and files that dont end in the extension
        for file in files:
            if getExtension(
                    file,
                    extensionFilter) and not file.startswith("."):
                dirList.append(root + "/" + file)

    if toFile is not None:
        with open(toFile, "w") as fileList:
            for file in dirList:
                fileList.write(file + "\n")

        return True
    else:
        return dirList


def remove(path):
    # to silince subprocess output by sending it to dev/null
    FNULL = open(os.devnull, "w")

    subprocess.call(
        "rm {}".format(path),
        shell=True,
        stdout=FNULL,
        stderr=subprocess.STDOUT)

    return True


def getExtension(filename, extension):
    if extension is None:
        return filename

    # reverse filename
    filename = filename[::-1]
    extractedExtension = ""

    for char in filename:
        extractedExtension = extractedExtension + char
        if char == ".":
            break

    # reverse backwards file extension
    extractedExtension = extractedExtension[::-1]
    if extension == extractedExtension:
        return True

    return False
