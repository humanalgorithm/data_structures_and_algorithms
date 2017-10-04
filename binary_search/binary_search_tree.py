import random
from . import print_description, SetupDemo


class node:
    left_node = None
    right_node = None
    value = None
    def __init__(self, value = None):
        self.left_node = None
        self.right_node = None
        self.value = value

#want to make binary search tree as follows:
'''
       8
    3     10
  2   4  9  12
'''
class BinarySearchTree():

    def setup_nodes(self):
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

        self.root.left_node = self.threeNode

        self.threeNode.left_node = self.twoNode
        self.threeNode.right_node = self.fourNode

        self.root.right_node = self.tenNode
        self.tenNode.right_node = self.twelveNode
        self.tenNode.left_node = self.nineNode
        self.twelveNode.right_node = self.fourteenNode
        self.fourteenNode.right_node = self.twentyNode

    def traverse_bst(self, startNode):

        if startNode.left_node == None and startNode.right_node == None:
            print "value: " + str(startNode.value)
            return
        #go down the left path
        if startNode.left_node !=None:
            print "value is: "  + str(startNode.value) + " <--- going left"
            self.traverse_bst(startNode.left_node)

        if startNode.right_node!=None:
            print "value is: "  + str(startNode.value) + " going right -->"
            self.traverse_bst(startNode.right_node)

    def validate_is_bst(self, startNode):
        if startNode.left_node == None and startNode.right_node == None:
            return True

        if startNode.left_node!=None:
            subtreeLess = self.is_subtree_lesser(startNode.value, startNode.left_node)
            leftBST = self.validate_is_bst(startNode.left_node)

        if startNode.right_node!=None:
           subtreeGreater = self.is_subtree_greater(startNode.value, startNode.right_node)
           rightBST = self.validate_is_bst(startNode.right_node)

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
        if startingNode.left_node == None and startingNode.right_node == None:
                return True
        left_lesser   = self.is_subtree_lesser(checkValue, startingNode.left_node)
        right_lesser = self.is_subtree_lesser(checkValue, startingNode.right_node)

        if left_lesser and right_lesser:
            return True
        else:
            return False

    def is_subtree_greater(self, checkValue, startingNode):

        if startingNode == None:
           return True
        if startingNode.value < checkValue:
            return False

        if startingNode.left_node == None and startingNode.right_node == None:
                return True
        left_greater = self.is_subtree_greater(checkValue, startingNode.left_node)
        right_greater = self.is_subtree_greater(checkValue, startingNode.right_node)

        if left_greater and right_greater:
            return True
        else:
            return False

    def get_greatest(self, nodeCurrent):

        while nodeCurrent.right_node!=None:
              nodeCurrent = nodeCurrent.right_node
        return nodeCurrent

    def get_least(self, nodeCurrent):

        while nodeCurrent.left_node!=None:
              nodeCurrent = nodeCurrent.left_node
        return nodeCurrent

    def delete_node(self, prev, nodeCurrent, nodeDelete):

        #################found element block#################
        if nodeCurrent.value == nodeDelete.value:
           #case 1 node to be deleted is a leaf
           if nodeCurrent.left_node == None and nodeCurrent.right_node == None:
               if prev.right_node == nodeCurrent:
                   prev.right_node = None
               else:
                  prev.left_node = None
               return
           #case 2 node to delete has only one child either on the right or on the left
           elif ((nodeCurrent.left_node!=None and nodeCurrent.right_node==None) or
                 (nodeCurrent.right_node!=None and nodeCurrent.left_node==None)):
                 #delete node has one left child
                 if nodeCurrent.left_node !=None:
                      prev.left_node = nodeCurrent.left_node
                 #delete node has one right child
                 elif nodeCurrent.right_node !=None:
                      prev.right_node = nodeCurrent.right_node
           #case 3 delete node has two children
           elif nodeCurrent.left_node!=None and nodeCurrent.right_node!=None:
                #get greatest node from lesser tree
                #either replace with greatest num from left tree or least num from right tree
                if random.choice([True, False]):
                    greatestLeft = self.get_greatest(nodeCurrent.left_node)
                    greatestLeftVal = greatestLeft.value
                    self.delete_node(None, self.root, greatestLeft)
                    nodeCurrent.value = greatestLeftVal
                else:
                    leastRight = self.get_least(nodeCurrent.right_node)
                    leastRightVal = leastRight.value
                    self.delete_node(None, self.root, leastRight)
                    nodeCurrent.value = leastRightVal
        ########################################################################

        ################continue traversal ###################
        elif nodeDelete.value < nodeCurrent.value:
            if nodeCurrent.left_node!=None:
               self.delete_node(nodeCurrent, nodeCurrent.left_node, nodeDelete)
            else:
               return
        elif nodeDelete.value > nodeCurrent.value:
            if nodeCurrent.right_node!=None:
                self.delete_node(nodeCurrent, nodeCurrent.right_node, nodeDelete)
            else:
                return

class BinarySearchTreeDemo(SetupDemo):
    def __init__(self):
        super(BinarySearchTreeDemo, self).setup_demo(__file__)

    def _run_valid_bst_checks(self, bst):
        print "check for is root left subtree lesser --> "
        result = str(bst.is_subtree_lesser(bst.root.value, bst.root.left_node))
        print result
        print ""
        print "check for is root right subtree greater -->"
        result = str(bst.is_subtree_greater(bst.root.value, bst.root.right_node))
        print result

        print " "
        print "check for is this a valid BST? -->"
        result = str(bst.validate_is_bst(bst.root))
        print result

    @print_description
    def valid_bst_checks(self):
        bst = BinarySearchTree()
        bst.setup_nodes()
        bst.traverse_bst(bst.root)
        self._run_valid_bst_checks(bst)

    @print_description
    def delete_14_node(self):
        bst = BinarySearchTree()
        bst.setup_nodes()
        bst.traverse_bst(bst.root)
        print "Deleting 14 node --->"
        bst.delete_node(None, bst.root, bst.fourteenNode)
        bst.traverse_bst(bst.root)
        self._run_valid_bst_checks(bst)

    @print_description
    def delete_root_node(self):
        bst = BinarySearchTree()
        bst.setup_nodes()
        bst.traverse_bst(bst.root)
        print "Deleting root node --->"
        bst.delete_node(None, bst.root, bst.root)
        bst.traverse_bst(bst.root)
        self._run_valid_bst_checks(bst)

    def delete_root_node_twice(self):
        bst = BinarySearchTree()
        bst.setup_nodes()
        bst.traverse_bst(bst.root)
        print "Deleting root node --->"
        bst.delete_node(None, bst.root, bst.root)
        print "Deleting root node again -->"
        bst.delete_node(None, bst.root, bst.root)
        self._run_valid_bst_checks(bst)


bst_demo = BinarySearchTreeDemo()
demos_to_run = [bst_demo.valid_bst_checks, bst_demo.delete_14_node, bst_demo.delete_root_node,
                bst_demo.delete_root_node_twice]
[func() for func in demos_to_run]


