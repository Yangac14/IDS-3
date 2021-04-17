import os
import re
import psutil
import pandas as pd
import numpy as np
alertcount = 0
previous = [0, 0, 0, 0, 0]


def filterFile(filename, search, fileout=None):
    file = pd.read_csv(os.getcwd() + "/Data/" + filename).values
    filteredFile = []
    for i in range(len(file)):
        if search in str(file[i]):
            print(str(file[i]))
            filteredFile.append(str(file[i]))

    filteredFile = pd.DataFrame(filteredFile)
    if fileout is not None:
        filteredFile.to_csv(os.getcwd() + "/Data/" + fileout)
    # uses file from Data folder and searches through line by line, prints the output, then optionally saves output


def printFile(filename, search=None):
    file = pd.read_csv(os.getcwd() + "/Data/" + filename).values

    for i in range(len(file)):
        if search in str(file[i]):
            print(str(file[i]))
    # prints specified file from data folder to console


def printDataFolder():
    files = os.listdir(os.getcwd() + "/Data/")

    for file in range(len(files)):
        print(file)
    # prints files in Data folder


def generateTSData(tstype, args, fileout):
    if tstype == "normal":  # assumes args are mean and sd and length
        data = np.random.normal(args[0], args[1], args[2])

    if tstype == "multi_normal":  # assumes args are trios of means, sds, and lengths
        data = np.random.normal(args[0], args[1], args[2])
        for i in range(3, len(args), 3):
            data = np.concatenate((data, np.random.normal(args[i], args[i + 1], args[i + 2])), axis=0)

    data = pd.DataFrame(data)
    data.to_csv(os.getcwd() + '/Data/' + fileout)
    # generates Time Series data of various types, the basic being type='normal'
    # wherin args would be the standard deviation and mean
    # and then the output file is the name where the data is saved


def testTSDistribution(filename, window_size, expected_mean, expected_sd, sd_error_range):
    file_df = pd.read_csv(os.getcwd() + "/Data/" + filename)

    comp = ((file_df.rolling(window_size) - expected_mean) / expected_sd)
    if np.any(abs(comp) > sd_error_range):
        print(filename + " fails test")

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
    rules = pd.read_csv(os.getcwd() + "/Data/Rules.csv")  # needs header column names to work
    rules.append([ruleName, expression, ruleError])
    rules.to_csv(os.getcwd() + "/Data/Rules.csv")
    # creates a search/filter rule using regex and saves it to a Rules.csv file


def applyRule(filename, ruleName, aggregate=False):
    file = pd.read_csv(os.getcwd() + "/Data/" + filename)
    Rules = pd.read_csv(os.getcwd() + "/Data/Rules.csv")
    rule = Rules[Rules["Name"] == ruleName][0]
    ruleExp = rule["Expression"]
    ruleError = rule["Error"]

    if aggregate:
        numErrors = 0
        for i in file:
            if file[i].contains(ruleExp):
                numErrors += 1
        print(numErrors, " x ", ruleError)
    else:
        for i in file:
            if file[i].contains(ruleExp):
                print(file[i], ruleError)
    # applies a rule from Rules.csv to a file


def abnormal(info, percent):
    sumed = 0
    if previous[0] == 0:
        for i in previous:
            previous[i] = info
    else:
        for i in range(4):
            sumed += previous[i]
        avg = sumed/4
        previous[4] = info
        if (avg*(1 + percent / 100) < previous[4]):
            print("Abnormal amount amount of processed data")
    for i in range(4):
        previous[i] = previous[i+1]



#takes an int and checks if it is abnormally larger than the previous inputs
def take_cpu():
    psutil.cpu_times()

def take_disk():
    psutil.disk_partitions()
def take_mem():
    psutil.virtual_memory()
 # responsile for finding the CPU data,Disk data, or memory data
def repeated_alerts():
    global alertcount
    if alertcount >= 2:
        print("Multiple alerts on a window, possible intruder detected")
#finds alerts on a program to check whether or not there are more than two
