from ui_helpers import *
from init import * 
from storyteller import *
from random import randint



def getSubject():
    subjectsPossible = ['john ', 'sammy ', 'the firetruck ', 'gaggles of geese ', 'LAZER TUWRTLEEZ ', 'tom ', 'a sack of explosives ', 'turtle ', 'hard drive ', 'a penguin ']
    subjectChosen1 = subjectsPossible[randint(0,9)]
    subjectChosen2 = subjectsPossible[randint(0,9)]
    subjects = [subjectChosen1, subjectChosen2]
    return subjects


def getAction():
    actionsPossible = ['pyrokenisifies ', 'swam to ', 'wiggles at ', 'discombobulates ', 'sliggerz away ', 'picks up ']
    actionChosen = actionsPossible[randint(0,5)]
    return actionChosen
    
    
def getFiller():
    fillers = ['the ', 'and ', 'so... ', 'FIRE PIGS ', 'wat ']
    filler = fillers[randint(0,4)]
    return filler

def constructSimpleClause(passedSubject = None):
    subjects = getSubject()
    if passedSubject == None:
        subject = subjects[0]
    elif passedSubject:
        subject = passedSubject
    subject2 = subjects[1]
    filler = getFiller()
    action = getAction()
    sentence = '' + str(subject) + str(action) + str(filler) + str(subject2)
    printS(sentence, .02)
    return subject