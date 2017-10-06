"""
Here we show several methods for going through a linked list backwards. We demonstrate 1) reversing the order by
iteratively reversing the links 2) traversing in reverse by using a stack and 3) using recursion to reverse the links
"""

from . import print_description, SetupDemo

class LinkedListNode:
    nextNode = None
    value = None
    def __init__(self, value=0, nextNode = None):
        self.nextNode = nextNode
        self.value = value

class LinkedListTraversal(object):
    def traverse_forwards_using_while_loop(self, head):
        node = head
        print node.value
        while node.nextNode!=None:
            node = node.nextNode
            print node.value

    def reverse_order_by_reversing_links(self, headIn):
        prev = None
        current = headIn
        current.nextNode
        while current != None:
            temp = current
            current = current.nextNode
            temp.nextNode = prev
            prev = temp
        return temp

    def traverse_reverse_using_stack(self, head):
        current = head
        stackTest = []
        while current!=None:
            stackTest.append(current)
            current = current.nextNode

        currentPop = stackTest.pop()
        while currentPop!=None:
            print currentPop.value
            currentPop = stackTest.pop() if len(stackTest) > 0 else None

    def reverse_order_using_recusion(self, prev, node):
        if node.nextNode == None:
            node.nextNode = prev
            return node
        head = self.reverse_order_using_recusion(node, node.nextNode)
        node.nextNode = prev
        return head


class LinkedListDemo(SetupDemo):
    def __init__(self):
        super(LinkedListDemo, self).setup_demo(__file__)
        self._setup_nodes()

    def _setup_nodes(self):
        self.node7 = LinkedListNode(120, None)
        self.node6 = LinkedListNode(50, self.node7)
        self.node5 = LinkedListNode(25, self.node6)
        self.node4 = LinkedListNode(200, self.node5)
        self.node3 = LinkedListNode(204, self.node4)
        self.node2 = LinkedListNode(130, self.node3)
        self.node1 = LinkedListNode(300, self.node2)

        self.head = self.node1

    @print_description
    def traverse_forwards_using_while_loop(self):
        self._setup_nodes()
        linked_list_traversal = LinkedListTraversal()
        print "traversing linked list forward starting with " + str(self.head.value)
        linked_list_traversal.traverse_forwards_using_while_loop(self.head)

    @print_description
    def traverse_reverse_using_stack(self):
        self._setup_nodes()
        linked_list_traversal = LinkedListTraversal()
        print "traversing linked list reverse starting with " + str(self.head.value)
        linked_list_traversal.traverse_reverse_using_stack(self.head)


    @print_description
    def reverse_order_by_reversing_links(self):
        self._setup_nodes()
        linked_list_traversal = LinkedListTraversal()
        print "linked list forward traversal before reverse"
        linked_list_traversal.traverse_forwards_using_while_loop(self.head)
        new_head = linked_list_traversal.reverse_order_by_reversing_links(self.head)
        print "linked list forward traversal after reversal"
        linked_list_traversal.traverse_forwards_using_while_loop(new_head)

    @print_description
    def reverse_order_using_recursion(self):
        self._setup_nodes()
        linked_list_traversal = LinkedListTraversal()
        print "linked list forward traversal before reverse"
        linked_list_traversal.traverse_forwards_using_while_loop(self.head)
        new_head = linked_list_traversal.reverse_order_using_recusion(None, self.head)
        print "linked list forward traversal after reversal"
        linked_list_traversal.traverse_forwards_using_while_loop(new_head)

if __name__ == "__main__":
    ll_demo = LinkedListDemo()
    demos_to_run = [ll_demo.traverse_forwards_using_while_loop, ll_demo.traverse_reverse_using_stack,
                    ll_demo.reverse_order_by_reversing_links, ll_demo.reverse_order_using_recursion]
    [func() for func in demos_to_run]

