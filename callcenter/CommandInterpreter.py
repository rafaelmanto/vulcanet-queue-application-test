import cmd

from callcenter.CallCenterManager import CallCenterManager


class CommandInterpreter(cmd.Cmd):
    def __init__(self, call_center_manager: CallCenterManager):
        self.manager = call_center_manager
        super().__init__()

    def do_call(self, args):
        self.manager.receive_call(args)

    def do_answer(self, args):
        self.manager.answer_call(args)

    def do_reject(self, args):
        self.manager.reject_call(args)

    def do_hangup(self, args):
        self.manager.hang_up_call(args)

    def preloop(self):
        print("Callcenter is on!")
        return

    def postloop(self):
        print("Callcenter is off :/")
