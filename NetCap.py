import virtualbox
import sys, os, subprocess, time
from sys import argv


timeSecs = 15 #Duration of each package to run

pcapPath = "/opt/log/tcpdump"  #this is the path that the file saves to - Change if you want it saved somewhere else


def checkArgv():

    L = argv[1:]
    print(L)
    if len(L) < 3:
        print("Error: Amount of Parameters are wrong: {} : tcp ip port".format(len(L)))
        return False,L
    else:
        L[0] = ("tcp")
    return True,L


def pathChecker(p): #checks path to see if its valid

    if not os.path.exists(p):
        os.directMake(p)
    return True


def tcpdump(p, n, d): #body function
    ErrCode = ""
    time_1 = time.strftime("_%m-%d_%H-%M-%S", time.localtime())
    name = na[1] + time_1 + "_" + na[0].upper()
    cmd1 = "tcpdump -i any -s 0 -w {0}/{1}.pcap {2} and ip host {3}".format(p, name, na[0], na[1])
    if int(na[2]) != 0:
        cmd1 = cmd1 + " and port {}".format(na[2])
    print(cmd1)

    else:
        ErrCode = "execute cmd OK; poll()={}  PID={}".format(pro.poll(),pro.pid)
        time.sleep(dudr)
    print(ErrCode)
    return ErrCode


if __name__ == '__main__':
    Ret,L == CheckArgv()
    if Ret == True:
        CheckPath(pathChecker)
        tcpdump(pathChecker, L, timeSecs)