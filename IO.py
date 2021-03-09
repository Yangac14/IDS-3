import os
import pandas as pd


def importCSV(filename=None):
    pass
    # if filename is none, open prompt window to find file
    # else use filename to import file, and save to Data folder

def importLog(filename=None):
    pass
    # if filename is none, open prompt window to find file
    # else use filename to import file, conver to csv, and save to Data folder

def PerformancePoll(filename, timeLen, timeInterval):
    pass
    # prints performance and saves it to file

def getFile():
    pass
    # function specifically for getting filenames already in Data folder using ui
    # open prompt window to find filename
    # then grab user input, using the filename in the right place
    # ie this function can be used to get a filename via filesystem ui rather than remembering name
    # and then passes it into a command such as searchFile