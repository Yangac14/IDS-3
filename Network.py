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
        try:
            cls.vbox = virtualbox.VirtualBox()
            cls.vb_session = virtualbox.Session()

            print([x.name for x in cls.vbox.machines])
            print("type intended vm name from above")
            cls.vm_name = input("#>")
            if cls.vm_name == "": cls.vm_name = "SecurityOnion"

            cls.vm = cls.vbox.find_machine(cls.vm_name)

            if cls.vm.state != 5:
                progress = cls.vm.launch_vm_process(cls.vb_session, "gui", [])
                progress.wait_for_completion()

            if cls.vb_session.state != 2:
                print("Session state is improperly locked, something went wrong.")
            else:
                print("logging into virtual machine")
                print("please enter vm root password")
                passwd = input("#>")  # getpass.getpass()
                cls.vm_access = cls.vb_session.console.guest.create_session("root", passwd)
        except Exception as e:
            print(e)

    # could abstract commands to the network class instead of calling network via other classes
    # @classmethod
    # def inputCommand(cls):
    #     pass
