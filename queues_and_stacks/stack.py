
import copy
from . import SetupDemo, print_description

class FILOStack(object):
    stack = []
    def __init__(self):
        self.stack = []

    def push(self, itemIn):
        self.stack.append(itemIn)

    def pop(self):
        length = len(self.stack)-1
        if length < 0:
            return None
        temp = copy.copy(self.stack[length])
        del(self.stack[length])
        return temp


class StackDemo(SetupDemo):
    def __init__(self):
        super(StackDemo, self).setup_demo()

    @print_description
    def test_1(self):
        pass