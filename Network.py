import virtualbox
import getpass

class VMConnection:
    vbox = None
    vb_session = None
    vm_name = None
    vm = None

    vm_access = None

    @classmethod
    def initialize(cls):
        cls.vbox = virtualbox.VirtualBox()
        cls.vb_session = virtualbox.Session()

        print([x.name for x in cls.vbox.machines])
        print("type intended vm name from above")
        cls.vm_name = input("#>")
        if cls.vm_name == "": vm_name = "SecurityOnion"

        cls.vm = cls.vbox.find_machine(cls.vm_name)

        if cls.machine.state != 5:
            progress = cls.machine.launch_vm_process(cls.vm_session, "gui", [])
            progress.wait_for_completion()

        if cls.vb_session.state != 2:
            print("Session state is improperly locked, something went wrong.")
        else:
            print("logging into virtual machine")
            print("please enter vm root password")
            cls.vm_access = cls.vb_session.console.guest.create_session("root", getpass.getpass())

    # could abstract commands to the network class instead of calling network via other classes
    # @classmethod
    # def inputCommand(cls):
    #     pass
