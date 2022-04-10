
from abc import ABCMeta, abstractmethod


class CallCenterManager(metaclass=ABCMeta):
    @abstractmethod
    def receive_call(self, call_id):
        pass

    @abstractmethod
    def answer_call(self, operator_id):
        pass

    @abstractmethod
    def reject_call(self, operator_id):
        pass

    @abstractmethod
    def hang_up_call(self, call_id):
        pass
