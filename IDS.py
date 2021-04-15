import virtualbox
import Commands
from Network import VMConnection

# initialize function can/will be used to initialize the vm
# and could be used to schedule various other functions (more important in sprint 2 I think)
def initalize():
    VMConnection.initialize()

# main loop that simply asks for user input
# later when setting up scheduled tasks or running other programs this will have to be broken up
# although ideally by this point we have a UI which will also change this a fair bit
def main():
    while True:
        Commands.Input(input("#>"))

if input("connect to VM? y/N:").lower() == 'y':
    initalize()
main()
