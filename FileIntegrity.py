import os

import pandas as pd
import hashlib

# adds file location to saved csv list to check
def specifyCriticalFile(fileloc=None):
    if fileloc is None:
        # open ui to find file
        pass

    integrityList = pd.read_csv(os.getcwd()+"/Data/integrityList.csv")
    integrityList.append(fileloc)
    integrityList.to_csv(os.getcwd()+"/Data/integrityList.csv")

# runs through the database of files, computing and storing their hashes
# code pretty much ripped from https://www.pythoncentral.io/hashing-files-with-python/
def initializeHashTable():
    BLOCKSIZE = 65536

    integrityList = pd.read_csv(os.getcwd()+"/Data/integrityList.csv")
    hashes = []
    for fileloc in integrityList:
        hasher = hashlib.sha3_512()
        with open(fileloc, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        hashes.append(hasher.hexdigest())

    hashes = pd.DataFrame(hashes)
    hashes.to_csv(os.getcwd()+"/Data/hashTable.csv")
    # probably could add a timestamp to this
    # also should add a universal file indexer and use that for indexing,
    # as otherwise changing the order of integrityList messes up parity with hashTable


# def checkHashTable():
#     pass
#     # doesn't need to be done yet
