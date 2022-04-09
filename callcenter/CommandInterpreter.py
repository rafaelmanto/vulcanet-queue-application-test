import cmd


class CommandInterpreter(cmd.Cmd):
    def __init__(self):
        super().__init__()

    def do_call(self, args):
        print("Calling")

    def do_answer(self, args):
        print("Answering")

    def do_reject(self, args):
        print("Reject")

    def do_hangup(self, args):
        print("Hangup")

    def preloop(self):
        print("Callcenter is on!")
        return

    def postloop(self):
        print("Callcenter is off :/")
