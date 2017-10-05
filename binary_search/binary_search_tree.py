import random
from . import print_description, SetupDemo, print_tree_from_breadth_first_stack

from depth_first_traversal import DepthFirstTraversal
from node import node

class BinarySearchTree():
    def __init__(self, root):
        self.root = root

    def validate_is_bst(self, startNode):
        if startNode.left == None and startNode.right == None:
            return True

        if startNode.left!=None:
            subtreeLess = self.is_subtree_lesser(startNode.value, startNode.left)
            leftBST = self.validate_is_bst(startNode.left)

        if startNode.right!=None:
           subtreeGreater = self.is_subtree_greater(startNode.value, startNode.right)
           rightBST = self.validate_is_bst(startNode.right)

        if ('leftBST' not in locals() or leftBST) and ('rightBST' not in locals() or rightBST) and  \
                ('subtreeLess' not in locals() or subtreeLess) and ('subtreeGreater' not in locals() or subtreeGreater):
           return True
        else:
            return False

    def is_subtree_lesser(self, checkValue, startingNode):

        if startingNode == None:
           return True
        if startingNode.value > checkValue:
            return False
        if startingNode.left == None and startingNode.right == None:
                return True
        left_lesser   = self.is_subtree_lesser(checkValue, startingNode.left)
        right_lesser = self.is_subtree_lesser(checkValue, startingNode.right)

        if left_lesser and right_lesser:
            return True
        else:
            return False

    def is_subtree_greater(self, checkValue, startingNode):

        if startingNode == None:
           return True
        if startingNode.value < checkValue:
            return False

        if startingNode.left == None and startingNode.right == None:
                return True
        left_greater = self.is_subtree_greater(checkValue, startingNode.left)
        right_greater = self.is_subtree_greater(checkValue, startingNode.right)

        if left_greater and right_greater:
            return True
        else:
            return False

    def get_greatest(self, nodeCurrent):

        while nodeCurrent.right!=None:
              nodeCurrent = nodeCurrent.right
        return nodeCurrent

    def get_least(self, nodeCurrent):

        while nodeCurrent.left!=None:
              nodeCurrent = nodeCurrent.left
        return nodeCurrent

    def delete_node(self, prev, nodeCurrent, nodeDelete):

        #################found element block#################
        if nodeCurrent.value == nodeDelete.value:
           #case 1 node to be deleted is a leaf
           if nodeCurrent.left == None and nodeCurrent.right == None:
               if prev.right == nodeCurrent:
                   prev.right = None
               else:
                  prev.left = None
               return
           #case 2 node to delete has only one child either on the right or on the left
           elif ((nodeCurrent.left!=None and nodeCurrent.right==None) or
                 (nodeCurrent.right!=None and nodeCurrent.left==None)):
                 #delete node has one left child
                 if nodeCurrent.left !=None:
                      prev.left = nodeCurrent.left
                 #delete node has one right child
                 elif nodeCurrent.right !=None:
                      prev.right = nodeCurrent.right
           #case 3 delete node has two children
           elif nodeCurrent.left!=None and nodeCurrent.right!=None:
                #get greatest node from lesser tree
                #either replace with greatest num from left tree or least num from right tree
                if random.choice([True, False]):
                    greatestLeft = self.get_greatest(nodeCurrent.left)
                    greatestLeftVal = greatestLeft.value
                    self.delete_node(None, self.root, greatestLeft)
                    nodeCurrent.value = greatestLeftVal
                else:
                    leastRight = self.get_least(nodeCurrent.right)
                    leastRightVal = leastRight.value
                    self.delete_node(None, self.root, leastRight)
                    nodeCurrent.value = leastRightVal
        ########################################################################

        ################continue traversal ###################
        elif nodeDelete.value < nodeCurrent.value:
            if nodeCurrent.left!=None:
               self.delete_node(nodeCurrent, nodeCurrent.left, nodeDelete)
            else:
               return
        elif nodeDelete.value > nodeCurrent.value:
            if nodeCurrent.right!=None:
                self.delete_node(nodeCurrent, nodeCurrent.right, nodeDelete)
            else:
                return

class BinarySearchTreeDemo(SetupDemo):
    def __init__(self):
        super(BinarySearchTreeDemo, self).setup_demo(__file__)

    def _run_valid_bst_checks(self, bst, root):
        print "check for is root left subtree lesser --> "
        result = str(bst.is_subtree_lesser(root.value, root.left))
        print result
        print ""
        print "check for is root right subtree greater -->"
        result = str(bst.is_subtree_greater(root.value, root.right))
        print result

        print " "
        print "check for is this a valid BST? -->"
        result = str(bst.validate_is_bst(root))
        print result

    def _print_tree(self, root):
        bst_levels_array = DepthFirstTraversal().depth_first_traversal_by_node(root)
        print_tree_from_breadth_first_stack(bst_levels_array, print_method="node")

    def _setup_nodes(self):
        self.eightNode = node(8)
        self.threeNode = node(3)
        self.twoNode = node(2)
        self.fourNode =  node(4)
        self.tenNode =  node(10)
        self.nineNode =  node(9)
        self.twelveNode = node(12)
        self.fourteenNode= node(14)
        self.twentyNode= node(20)
        self.root = self.eightNode

        self.root.left = self.threeNode

        self.threeNode.left = self.twoNode
        self.threeNode.right = self.fourNode

        self.root.right = self.tenNode
        self.tenNode.right = self.twelveNode
        self.tenNode.left = self.nineNode
        return self.root

    @print_description
    def valid_bst_checks(self):
        self._setup_nodes()
        bst = BinarySearchTree(self.root)
        print "tree is -->"
        self._print_tree(self.root)
        self._run_valid_bst_checks(bst, self.root)

    @print_description
    def delete_10_node(self):
        self._setup_nodes()
        bst = BinarySearchTree(self.root)
        print "tree is -->"
        self._print_tree(self.root)
        print "Deleting 10 node --->"
        bst.delete_node(None, self.root, self.tenNode)
        print "tree is -->"
        self._print_tree(self.root)
        self._run_valid_bst_checks(bst, self.root)

    @print_description
    def delete_root_node(self):
        self._setup_nodes()
        bst = BinarySearchTree(self.root)
        self._print_tree(self.root)
        print "Deleting root node --->"
        bst.delete_node(None, self.root, self.root)
        self._print_tree(self.root)
        self._run_valid_bst_checks(bst, self.root)

    def delete_root_node_twice(self):
        self._setup_nodes()
        bst = BinarySearchTree(self.root)
        self._print_tree(self.root)
        print "Deleting root node --->"
        bst.delete_node(None, self.root, self.root)
        self._print_tree(self.root)
        print "Deleting root node again -->"
        bst.delete_node(None, self.root, self.root)
        self._print_tree(self.root)
        self._run_valid_bst_checks(bst, self.root)

if __name__ == "__main__":
    bst_demo = BinarySearchTreeDemo()
    demos_to_run = [bst_demo.valid_bst_checks, bst_demo.delete_10_node, bst_demo.delete_root_node
                    ,bst_demo.delete_root_node_twice]
    [func() for func in demos_to_run]