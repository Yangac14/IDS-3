import sys

import Analysis
import FileIntegrity
import IO


# the main program input parser. essentially just elifs directing to other classes and functions
# the first input is the command, while the rest are arguments to the command such as
# #>importCSV
def Input(usrInput):
    usrInput = usrInput.split(" ")
    command = usrInput[0]
    args = usrInput[1:]
    # note: the system of using args for remaining variables can be simplified
    # ideally it should use a tuple which can be expanded in place to fill method arguments
    # without worrying out assuming the len of args
    # the train of elifs could also be replaced with switch cases

    if command == "quit":
        sys.quit()
    elif command == "importCSV":
        if args:
            IO.importCSV(args[0])
        else:
            IO.importCSV()
    elif command == "importLog":
        if args:
            IO.importLog(args[0])
        else:
            IO.importLog()
    elif command == "performancePoll" or command == "perfPoll":
        IO.perfPoll(args[0], args[1], args[2])
    elif command == "filterFile":
        if len(args) > 2:
            Analysis.filterFile(args[0], args[1], args[2])
    elif command == "printFile":
        if args:
            if len(args > 1):
                Analysis.printFile(args[0], args[1])
            else:
                Analysis.printFile(args[0])
        else:
            print("error no filename argument is passed.")
    elif command == "generateTSData":
        Analysis.generateTSData(args[0], args[1:-1], args[-1])
    elif command == "specifyCriticalFile":
        FileIntegrity.specifyCriticalFile(args[0])
    elif command == "initializeHashTable":
        FileIntegrity.initializeHashTable()
