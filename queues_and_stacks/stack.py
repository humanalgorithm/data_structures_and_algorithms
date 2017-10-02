import copy
class stack:
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
