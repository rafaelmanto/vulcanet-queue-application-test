from CommandInterpreter import CommandInterpreter
from callcenter.LocalCallCenterManager import LocalCallCenterManager

if __name__ == '__main__':
    CommandInterpreter(LocalCallCenterManager()).cmdloop()
