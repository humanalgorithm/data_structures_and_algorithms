
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
        super(StackDemo, self).setup_demo(__file__)

    def _print_stack(self, stack):
        print "Stack is --> ", stack.stack

    def _print_pushing_item(self, element):
        print "Appending element ", element

    def _print_stack_status(self, stack):
        print "Stack currently is -- >"
        for element in stack.stack:
            print "        |" + str(element) + "|,"

    def _print_pop_messagge(self, element):
        print "Popping from stack and got element --> ", element

    @print_description
    def push_five_items_then_pop_five_items(self):
        stack = FILOStack()
        elements = [5, 90, 303, 500, 1010]
        for element in elements:
            self._print_pushing_item(element)
            stack.push(element)
            self._print_stack_status(stack)

    @print_description
    def push_four_then_pop_four(self):
        stack = FILOStack()
        elements = ['A', 'B', 'C', 'D']
        for element in elements:
            self._print_pushing_item(element)
            stack.push(element)
            self._print_stack_status(stack)

        for i in range(0, len(elements)):
            element = stack.pop()
            self._print_pop_messagge(element)
            self._print_stack_status(stack)

if __name__ == "__main__":
    stack_demo = StackDemo()
    demos_to_run = [stack_demo.push_five_items_then_pop_five_items, stack_demo.push_four_then_pop_four]
    [func() for func in demos_to_run]