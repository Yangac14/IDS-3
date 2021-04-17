import os
import pandas as pd

from Network import VMConnection



# import functions below need to differentiate between host fs and vm fs for file searching

def importCSV(filename=None):
    if filename is None:
        pass
    # if filename is none, open prompt window to find file
    else:
        file = pd.read_csv(filename)
        file.to_csv(os.getcwd() + "/Data/" + filename.split('/')[-1])
    # else use filename to import file, and save to Data folder


def importLog(filename=None):
    if filename is None:
        pass
    #     # if filename is none, open prompt window to find file
    #     else:
    #         file = pd.read_csv(filename)
    #         file.to_csv(os.getcwd() + "/Data/" + filename.split('/')[-1].split('.')[0])
    #         # might convert implicitly - needs testing
    #     # else use filename to import file, convert to csv, and save to Data folder
    #
    # # ssh logs can be extracted from /var/log/auth.log
    #
    #
    # def perfPoll(timeLen, timeInterval, fileout):
    #     VMConnection.vm_access.execute("usr/bin/vmstat", [str(timeLen), str(timeInterval), ">",
    #                                                       "/media/sf_Data/" + fileout])  # .split('.')[0] + ".csv"
    #     # potential alternative to having to direct through /bin/example for commands would be to create scripts
    # in the shared data folder that can be ran using this process

# def getFile():
#     pass
#     # function specifically for getting filenames already in Data folder using ui
#     # open prompt window to find filename
#     # then grab user input, using the filename in the right place
#     # ie this function can be used to get a filename via filesystem ui rather than remembering name
#     # and then passes it into a command such as searchFile
