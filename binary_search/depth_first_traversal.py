'''
Depth first traversal
'''

from __init__ import print_description, SetupDemo, print_tree_from_breadth_first_stack
from node import node

class DepthFirstTraversal(object):
    def depth_first_traversal_by_node(self, current):
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

    def depth_first_traversal_by_element(self, bst_array):
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


class DepthFirstTraversalDemo(SetupDemo):
    def __init__(self):
        super(DepthFirstTraversalDemo, self).setup_demo(__file__)

        self.binary_search_tree_elements_level_order = [14, 10, 18, 4, 12, 16, 20, 3, 5, 11, 13, 15, 17, 19, 22]
    def _setup_nodes(self):
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

    @print_description
    def depth_first_traversal_through_elements(self):
        depth_first_traversal = DepthFirstTraversal()
        print "Elements in level are :"
        print self.binary_search_tree_elements_level_order
        print " "
        result = depth_first_traversal.depth_first_traversal_by_element(self.binary_search_tree_elements_level_order)
        print "resulting depth first stack after traversal is"
        print result
        print_tree_from_breadth_first_stack(result)

    @print_description
    def depth_first_traversal_through_nodes(self):
        self.root = self._setup_nodes()
        depth_first_traversal = DepthFirstTraversal()
        print "Values of nodes to print are "
        print self.binary_search_tree_elements_level_order
        print " "
        stack = depth_first_traversal.depth_first_traversal_by_node(self.root)
        print "resulting stack is "
        print [node.value for node in stack]
        print "Tree is --> "
        print_tree_from_breadth_first_stack(stack, print_method="node")

if __name__ == "__main__":
    depth_first_demo = DepthFirstTraversalDemo()
    demos_to_run = [depth_first_demo.depth_first_traversal_through_elements,
                    depth_first_demo.depth_first_traversal_through_nodes]
    [func() for func in demos_to_run]