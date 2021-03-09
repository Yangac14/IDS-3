import sys

import IO

# the main program input parser. essentially just elifs directing to other classes and functions
# the first input is the command, while the rest are arguments to the command such as
# #>importCSV
def Input(input):
    input = input.split(" ")
    command = input[0]
    args = input[1:]

    if command == "quit":
        sys.quit()
    elif command == "importCSV":
        if args: IO.importCSV(args[0])
        else: IO.importCSV()
    elif command == "importLog":
        if args: IO.importLog(args[0])
        else: IO.importLog()
    elif command == "printFile":
        if args:
            if len(args > 1):
                IO.importLog(args[0], args[1])
            else:
                IO.importLog(args[0])
        else:
            print("error no filename argument is passed.")
    elif command == "":
        pass
