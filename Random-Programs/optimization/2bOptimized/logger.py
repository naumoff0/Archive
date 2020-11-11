import datetime
import time
import os
import sys

# get user's current directory

directory = os.path.dirname(os.path.realpath(__file__)) + '/logs'


def createNewLog():

    # ensure log folder exists

    if not os.path.exists(directory):
        os.mkdir(directory)

    # get timestamp for naming the log

    timeInSeconds = time.time()
    timestamp = \
        datetime.datetime.fromtimestamp(timeInSeconds).strftime('%Y-%m-%d %H:%M:%S'
            )

    logFile = directory + '/' + timestamp + '.txt'
    mostRecentLog = directory + '/mostRecentLog.txt'

    # create log file and file with the log file's name

    with open(logFile, 'w') as log:
        with open(mostRecentLog, 'w') as recentLog:
            recentLog.write(timestamp)


def findMostRecentLog():

    # ensure logger has been intiated

    try:
        with open(directory + '/mostRecentLog.txt', 'r') as logFile:
            logName = logFile.read()
    except FileNotFoundError:

        print("Must initiate logger first!")
        sys.exit(1)

    return directory + '/' + logName + '.txt'


def log(comment):
    comment = str(comment)

    # write to log file retriving most recent log from corresponding file

    with open(findMostRecentLog(), 'a') as log:
        log.write(comment + '\n')
