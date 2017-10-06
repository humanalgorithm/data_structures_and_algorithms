"""
In this demo we build the behavior of a queue data structure by using two stacks. Recall that a queue is a
First in-first out data structure whereas a stack is a first in-last out data structure. In order to get the behavior of a
queue with two stacks we reverse the order of the first stack by popping all of the elements out and pushing them into
the second stack before adding any elements. Then when we want to get an element we pop from the first stack.
Essentially what we are doing here is using the second stack as a temporary holder to reverse the first stack
whenever we want to add another element.
"""
from stack import FILOStack

from . import SetupDemo, print_description


class QueueUsingStacks(object):
    def add_element(self, element, stack1, stack2):
        current = stack1.pop()
        while current != None:
            stack2.push(current)
            current = stack1.pop()

        stack2.push(element)

    def get_next_element(self, stack1, stack2):
        current = stack2.pop()
        while current != None:
            stack1.push(current)
            current = stack2.pop()

        return str(stack1.pop())


class QueueUsingStacksDemo(SetupDemo):
    def __init__(self):
        super(QueueUsingStacksDemo, self).setup_demo(__file__)

    def _print_add_one_element(self, element, stack1, stack2):
        print "adding element " + str(element)
        self._print_stacks_status(stack1, stack2)

    def _print_stacks_status(self, stack1, stack2):
        print "FILO Stack 1 is currently --> ", str(stack1.stack)
        print "FILO Stack 2 is currently --> ", str(stack2.stack)

    def _process_item_message(self, next_element):
        print "Processing item from queue and get --> ", next_element

    def _print_FIFO_order_message(self, elements):
        print "To process these in FIFO order we would want to read in the order --> ", str(elements)

    def _print_processing_item(self, next_element):
        print "Processing item from queue and get --> ", next_element

    def _add_elements(self, queue_stack, elements, stack1, stack2):
        for element in elements:
            queue_stack.add_element(element, stack1, stack2)
            self._print_add_one_element(element, stack1, stack2)

    def _process_number_of_items(self, queue_stack, num_elements, stack1, stack2):
        for i in range(0, num_elements):
            next_element = queue_stack.get_next_element(stack1, stack2)
            self._print_processing_item(next_element)
            self._print_stacks_status(stack1, stack2)

    def _add_one_element(self, queue_stack, element_add, stack1, stack2):
        queue_stack.add_element(element_add, stack1, stack2)
        self._print_add_one_element(element_add, stack1, stack2)

    @print_description
    def add_4_elements_and_then_process_them_all(self):
        stack1 = FILOStack()
        stack2 = FILOStack()
        queue_stack = QueueUsingStacks()
        elements = [1, 2, 3, 4]
        self._add_elements(queue_stack, elements, stack1, stack2)
        self._print_FIFO_order_message(elements)
        self._process_number_of_items(queue_stack, len(elements), stack1, stack2)

    @print_description
    def add_two_elements_process_two_then_add_two_more_then_proces_remaining_two(self):
        stack1 = FILOStack()
        stack2 = FILOStack()
        queue_stack = QueueUsingStacks()
        elements = [5, 18]
        self._add_elements(queue_stack, elements, stack1, stack2)
        self._print_FIFO_order_message(elements)
        self._process_number_of_items(queue_stack, 2, stack1, stack2)

        self._add_one_element(queue_stack, 101, stack1, stack2)
        self._add_one_element(queue_stack, 102, stack1, stack2)

        self._process_number_of_items(queue_stack, len(stack2.stack), stack1, stack2)

    @print_description
    def add_two_process_one_add_one_one_process_one_add_one_process_one(self):
        stack1 = FILOStack()
        stack2 = FILOStack()
        queue_stack = QueueUsingStacks()
        elements = ['A', 'B']
        self._add_elements(queue_stack, elements, stack1, stack2)
        self._print_FIFO_order_message(elements)
        self._process_number_of_items(queue_stack, 1, stack1, stack2)

        self._add_one_element(queue_stack, 'C', stack1, stack2)
        self._process_number_of_items(queue_stack, 1, stack1, stack2)

        self._add_one_element(queue_stack, 'D', stack1, stack2)
        self._process_number_of_items(queue_stack, 1, stack1, stack2)

        self._process_number_of_items(queue_stack, 1, stack1, stack2)


if __name__ == "__main__":
    queue_stack_demo = QueueUsingStacksDemo()
    demos_to_run = [queue_stack_demo.add_4_elements_and_then_process_them_all,
                    queue_stack_demo.add_two_elements_process_two_then_add_two_more_then_proces_remaining_two,
                    queue_stack_demo.add_two_process_one_add_one_one_process_one_add_one_process_one]
    [func() for func in demos_to_run]
