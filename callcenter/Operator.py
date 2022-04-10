from enum import IntEnum


class OperatorStatus(IntEnum):
    AVAILABLE = 0
    RINGING = 1
    BUSY = 1


class Operator:
    def __init__(self, identifier: str):
        self.__id = identifier
        self._status = OperatorStatus.AVAILABLE
        self.current_call_id = None

    def __lt__(self, other):
        if isinstance(other, Operator):
            if self.status == other.status:
                return self.__id < other.__id
            else:
                return self.status < other.status
        else:
            # TODO Return something that indicates a wrong comparison
            print("Wrong comparison")

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status: OperatorStatus):
        if new_status in OperatorStatus:
            self._status = new_status
