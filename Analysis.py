import os
import pandas as pd
import numpy as np


def filterFile(filename, search, output=None):
    pass
    # uses file from Data folder and searches through line by line, prints the output, then optionally saves output

def printFile(filename, search=None):
    pass
    # prints file from data folder

def generateTSData(type, length, args, filename):
    pass
    # generates Time Series data of various types, the basic being type='normal'
    # wherin args would be the standard deviation and mean
    # and then the output file is the name where the data is saved

def createTSRule(window_size, expression, name):
    pass
    # creates a time series rule using regex and saves it to a TSRules.csv file

def applyTSRule(filename, ruleName):
    pass
    # applies a rule from TSRules.csv to a file

def createRule(expression):
    pass
    # creates a search/filter rule using regex and saves it to a Rules.csv file

def applyRule(filename, ruleName):
    pass
    # applies a rule from Rules.csv to a file
