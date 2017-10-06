'''
Breadth First traversal of a binary search tree is when you print all of the elements at each level before moving on
to the next. In this way we end up printing across the tree from left to right at each level. One way to accomplish this
is to use a stack to iteratively append the root element, its left and right child and then do the same for the left
and right nodes. In this demo we demonstrate breadth first traversal using an array of elements ordered to simulate
a binary search tree and an actuial binary search tree with the nodes connected to each other.
tree
'''

from __init__ import print_description, SetupDemo, print_tree_from_breadth_first_stack
from node import node

class BreadthFirstTraversal(object):
    def breadth_first_traversal_by_node(self, current):
        stack = []
        if current == None:
            return

        stack.append(current)
        i = 0
        while stack[i].left or stack[i].right:
            stack.append(stack[i].left) if stack[i] else stack.append(None)
            stack.append(stack[i].right) if stack[i] else stack.append(None)
            i = i + 1
        return [node for node in stack]

    def breadth_first_traversal_by_element(self, bst_array):
        if bst_array == None:
            return None

        def _get_left(bst_array, index):
            # to go left --> index  * 2 +1
            computed_index = (index * 2) + 1
            if computed_index < len(bst_array):
                return bst_array[computed_index]
            else: return None

        def _get_right(bst_array, index):
            # to go right --> index *2 + 2
            computed_index = (index * 2) + 2
            if computed_index < len(bst_array):
                return bst_array[computed_index]
            else: return None

        stack = []
        if len(bst_array) == 0:
            return
        stack.append(bst_array[0])

        for i in range(0, len(bst_array)/2):
            stack.append(_get_left(bst_array, index=i))
            stack.append(_get_right(bst_array, index=i))
        return stack


class BreadthFirstTraversalDemo(SetupDemo):
    def __init__(self):
        super(BreadthFirstTraversalDemo, self).setup_demo(__file__)

        self.binary_search_tree_elements_level_order = [14, 10, 18, 4, 12, 16, 20, 3, 5, 11, 13, 15, 17, 19, 22]
    def _setup_nodes(self):
        #target tree to set up is:
        '''
                      14
                10             18
             4       12      16    20
           3   5   11 13    15 17 19 22
        '''
        self.fourteen_node = node(14)
        self.ten_node = node(10)
        self.eighteen_node = node(18)
        self.four_node = node(4)
        self.twelve_node = node(12)
        self.sixteen_node = node(16)
        self.twenty_node = node(20)
        self.three_node = node(3)
        self.five_node = node(5)
        self.eleven_node = node(11)
        self.thirteen_node = node(13)
        self.fifteen_node = node(15)
        self.seventeen_node = node(17)
        self.nineteen_node = node(19)
        self.twenty_two_node = node(22)
        #level 1
        self.fourteen_node.left = self.ten_node
        self.fourteen_node.right = self.eighteen_node
        #level2
        self.ten_node.left = self.four_node
        self.ten_node.right = self.twelve_node
        self.eighteen_node.left = self.sixteen_node
        self.eighteen_node.right = self.twenty_node
        #level 3
        self.four_node.left = self.three_node
        self.four_node.right = self.five_node
        self.twelve_node.left = self.eleven_node
        self.twelve_node.right = self.thirteen_node
        self.sixteen_node.left = self.fifteen_node
        self.sixteen_node.right = self.seventeen_node
        self.twenty_node.left = self.nineteen_node
        self.twenty_node.right = self.twenty_two_node

        self.root = self.fourteen_node
        return self.root

    def _log_search_tree_array(self, level_array):
        print "Values in level order in array format is :"
        print level_array
        print " "

    def _log_result_from_element_traversal(self, stack_result):
        print "resulting breadth first stack after traversal is"
        print stack_result
        print "stack print is --> "
        print_tree_from_breadth_first_stack(stack_result)

    def _log_result_from_node_traversal(self, stack_result):
        print "resulting breadth first stack after traversal is"
        print [node.value for node in stack_result]
        print "stack print is --> "
        print_tree_from_breadth_first_stack(stack_result, print_method="node")

    @print_description
    def breadth_first_traversal_through_elements(self):
        breadth_first_traversal = BreadthFirstTraversal()
        self._log_search_tree_array(self.binary_search_tree_elements_level_order)
        stack_result = breadth_first_traversal.breadth_first_traversal_by_element(self.binary_search_tree_elements_level_order)
        self._log_result_from_element_traversal(stack_result)

    @print_description
    def breadth_first_traversal_through_nodes(self):
        self.root = self._setup_nodes()
        breadth_first_traversal = BreadthFirstTraversal()
        self._log_search_tree_array(self.binary_search_tree_elements_level_order)
        stack_result = breadth_first_traversal.breadth_first_traversal_by_node(self.root)
        self._log_result_from_node_traversal(stack_result)

if __name__ == "__main__":
    breadth_first_demo = BreadthFirstTraversalDemo()
    demos_to_run = [breadth_first_demo.breadth_first_traversal_through_elements,
                    breadth_first_demo.breadth_first_traversal_through_nodes]
    [func() for func in demos_to_run]