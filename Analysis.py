import os
import re

import pandas as pd
import numpy as np


def filterFile(filename, search, fileout=None):
    file = pd.read_csv(os.getcwd() + "/Data/" + filename).values
    filteredFile = []
    for i in range(len(file)):
        if search in str(file[i]):
            print(str(file[i]))
            filteredFile.append(str(file[i]))

    filteredFile = pd.DataFrame(filteredFile)
    if fileout is not None:
        filteredFile.to_csv(os.getcwd()+"/Data/"+fileout)
    # uses file from Data folder and searches through line by line, prints the output, then optionally saves output


def printFile(filename, search=None):
    file = pd.read_csv(os.getcwd() + "/Data/" + filename).values

    for i in range(len(file)):
        if search in str(file[i]):
            print(str(file[i]))
    # prints file from data folder to console


def generateTSData(tstype, args, fileout):
    if tstype == "normal":  # assumes args are mean and sd and length
        data = np.random.normal(args[0], args[1], args[2])

    if tstype == "multi_normal":  # assumes args are trios of means, sds, and lengths
        data = np.random.normal(args[0], args[1], args[2])
        for i in range(3, len(args), 3):
            data = np.concatenate((data,np.random.normal(args[i], args[i+1], args[i+2])), axis=0)

    data = pd.DataFrame(data)
    data.to_csv(os.getcwd() + '/Data/' + fileout)
    # generates Time Series data of various types, the basic being type='normal'
    # wherin args would be the standard deviation and mean
    # and then the output file is the name where the data is saved


# def createTSRule(window_size, expression, name):
#     pass
#     # creates a time series rule using regex and saves it to a TSRules.csv file
#
#
# def applyTSRule(filename, ruleName):
#     pass
#     # applies a rule from TSRules.csv to a file
#
#
def createRule(expression, ruleName, ruleError):
    rules = pd.read_csv(os.getcwd()+"/Data/Rules.csv") # needs header column names to work
    rules.append([ruleName, expression, ruleError])
    rules.to_csv(os.getcwd()+"/Data/Rules.csv")
    # creates a search/filter rule using regex and saves it to a Rules.csv file


def applyRule(filename, ruleName):
    file = pd.read_csv(os.getcwd()+"/Data/"+filename)
    Rules = pd.read_csv(os.getcwd()+"/Data/Rules.csv")
    rule = Rules[Rules["Name"] == ruleName][0]
    ruleExp = rule["Expression"]
    ruleError = rule["Error"]

    for i in file:
        if file[i].contains(ruleExp):
            print(file[i], ruleError)
    # applies a rule from Rules.csv to a file
