""" file management module """
import linecache
import os
import random
import subprocess


def find(file_filter=None, output=None):
    """ finds files """

    # find base directory
    path = os.getcwd()

    directories = []
    for root, _, files in os.walk(path):
        # filter out hidden files and files that dont end in the extension
        for file in files:
            if extract_extension(file, file_filter) and not file.startswith("."):
                directories.append(root + "/" + file)

    if output is not None:
        with open(output, "w") as file_list:
            for file in directories:
                file_list.write(file + "\n")

        return

    return directories


def remove(path):
    """ removes a file """

    if os.path.exists(path.strip()):
        if os.path.isdir(path):
            subprocess.call("rm -rf {}".format(path), shell=True)
            return

        subprocess.call("rm {}".format(path), shell=True)


def extract_extension(filename, extension):
    """ filters out files with specific extensions like .py or .txt or even entire filenames """

    if not extension:
        return filename

    # reverse filename
    filename = filename[::-1]
    extracted = ""

    for char in filename:
        extracted = extracted + char
        # reverse backwards file extension
        if extracted[::-1] == extension:
            return True


def retrive(file_name, *lines):
    """ finds and retrives lines from a file. use ALL to retrive all lines"""

    path = find(file_name)
    retrieved = []

    for line in list(lines):
        # if all lines has been requested
        if line == "ALL":
            with open(*path, "r") as file:
                for line in file:
                    retrieved.append(line.strip())

            break

        elif line == "RANDOM":
            return linecache.getline(*path, random.randint(1, sum(1 for line in open(*path)))).strip()

        else:
            retrieved.append(linecache.getline(file_name, line))

    return retrieved
