import queue
import heapq
from callcenter.CallCenterManager import CallCenterManager
from callcenter.Operator import OperatorStatus, Operator


class LocalCallCenterManager(CallCenterManager):
    def __init__(self):
        self.__callQueue = queue.Queue()
        self.__current_calls_assignment = {}
        self.__operators_dict = {
            "A": Operator("A"),
            "B": Operator("B")
        }
        self.__operators_heapq = list(self.__operators_dict.values())
        heapq.heapify(self.__operators_heapq)

    def __assign_call(self, call_id):
        most_available_operator = self.__operators_heapq[0]
        if most_available_operator.status == OperatorStatus.AVAILABLE:
            most_available_operator.status = OperatorStatus.RINGING
            most_available_operator.current_call_id = call_id
            self.__current_calls_assignment[call_id] = most_available_operator
            heapq.heapify(self.__operators_heapq)
            print(f"Call {call_id} ringing for operator {most_available_operator.id}")

    def __free_operator(self, operator, post_free_msg):
        operator.status = OperatorStatus.AVAILABLE
        del self.__current_calls_assignment[operator.current_call_id]
        operator.current_call_id = None
        heapq.heapify(self.__operators_heapq)
        print(post_free_msg)
        if self.__callQueue.not_empty:
            self.__assign_call(self.__callQueue.get())

    def receive_call(self, call_id):
        print(f"Call {call_id} received")
        self.__assign_call(call_id)
        if self.__current_calls_assignment.get(call_id) is None:
            self.__callQueue.put(call_id)
            print(f"Call {call_id} waiting in queue")

    def answer_call(self, operator_id):
        operator = self.__operators_dict.get(operator_id)
        if operator.status == OperatorStatus.RINGING:
            operator.status = OperatorStatus.BUSY
            heapq.heapify(self.__operators_heapq)
            print(f"Call {operator.current_call_id} answered by operator {operator_id}")
        else:
            print(f"There is nothing for operator {operator_id} to answer")

    def reject_call(self, operator_id):
        operator = self.__operators_dict.get(operator_id)
        if operator.status == OperatorStatus.RINGING:
            msg = f"Call {operator.current_call_id} rejected by operator {operator_id}"
            self.__free_operator(operator, msg)
            heapq.heapify(self.__operators_heapq)
        else:
            print(f"There is nothing for operator {operator_id} to reject")

    def hang_up_call(self, call_id):
        operator_on_call = self.__current_calls_assignment.get(call_id)
        msg = f"Call {call_id} missed"

        if isinstance(operator_on_call, Operator):
            if operator_on_call.status == OperatorStatus.BUSY:
                msg = f"Call {call_id} finished and operator {operator_on_call.id} available"
            self.__free_operator(operator_on_call, msg)
            return

        print(msg)
