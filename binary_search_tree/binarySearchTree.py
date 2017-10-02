import random

class node:
    left_node = None
    right_node = None
    value = None
    def __init__(self, value = None):
        self.left_node = None
        self.right_node = None
        self.value = value


#want to make binary search treer as follows:
'''
       8
    3     10
  2   4  9  12
'''
class bst():

    def setupNodes(self):
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

    def traverseBST(self, startNode):

        if startNode.left_node == None and startNode.right_node == None:
            print "value: " + str(startNode.value)
            return
        #go down the left path
        if startNode.left_node !=None:
            print "value is: "  + str(startNode.value) + " <--- going left"
            self.traverseBST(startNode.left_node)

        if startNode.right_node!=None:
            print "value is: "  + str(startNode.value) + " going right -->"
            self.traverseBST(startNode.right_node)

    def checkBST(self, startNode):
        if startNode.left_node == None and startNode.right_node == None:
            return True

        if startNode.left_node!=None:
            subtreeLess = self.isSubtreeLesser(startNode.value, startNode.left_node)
            leftBST = self.checkBST(startNode.left_node)

        if startNode.right_node!=None:
           subtreeGreater = self.isSubtreeGreater(startNode.value, startNode.right_node)
           rightBST = self.checkBST(startNode.right_node)

        if ('leftBST' not in locals() or leftBST) and ('rightBST' not in locals() or rightBST) and  \
                ('subtreeLess' not in locals() or subtreeLess) and ('subtreeGreater' not in locals() or subtreeGreater):
           return True
        else:
            return False

    def isSubtreeLesser(self, checkValue, startingNode):

        if startingNode == None:
           return True
        if startingNode.value > checkValue:
            return False
        if startingNode.left_node == None and startingNode.right_node == None:
                return True
        leftlesser   = self.isSubtreeLesser(checkValue, startingNode.left_node)
        rightlesser = self.isSubtreeLesser(checkValue, startingNode.right_node)

        if leftlesser and rightlesser:
            return True
        else:
            return False

    def isSubtreeGreater(self, checkValue, startingNode):

        if startingNode == None:
           return True
        if startingNode.value < checkValue:
            return False

        if startingNode.left_node == None and startingNode.right_node == None:
                return True
        leftGreater   = self.isSubtreeGreater(checkValue, startingNode.left_node)
        rightGreater = self.isSubtreeGreater(checkValue, startingNode.right_node)

        if leftGreater and rightGreater:
            return True
        else:
            return False

    def getGreatest(self, nodeCurrent):

        while nodeCurrent.right_node!=None:
              nodeCurrent = nodeCurrent.right_node
        return nodeCurrent

    def getLeast(self, nodeCurrent):

        while nodeCurrent.left_node!=None:
              nodeCurrent = nodeCurrent.left_node
        return nodeCurrent

    def deleteNode(self, prev, nodeCurrent, nodeDelete):

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
                    greatestLeft = self.getGreatest(nodeCurrent.left_node)
                    greatestLeftVal = greatestLeft.value
                    self.deleteNode(None, self.root, greatestLeft)
                    nodeCurrent.value = greatestLeftVal
                else:
                    leastRight = self.getLeast(nodeCurrent.right_node)
                    leastRightVal = leastRight.value
                    self.deleteNode(None, self.root, leastRight)
                    nodeCurrent.value = leastRightVal
        ########################################################################

        ################continue traversal ###################
        elif nodeDelete.value < nodeCurrent.value:
            if nodeCurrent.left_node!=None:
               self.deleteNode(nodeCurrent, nodeCurrent.left_node, nodeDelete)
            else:
               return
        elif nodeDelete.value > nodeCurrent.value:
            if nodeCurrent.right_node!=None:
                self.deleteNode(nodeCurrent, nodeCurrent.right_node, nodeDelete)
            else:
                return
print "------setting up BST-----"
bst = bst()
bst.setupNodes()
print "-----original BST------"
bst.traverseBST(bst.root)
print ""
print "--is root left subtree lesser? " + str(bst.isSubtreeLesser(bst.root.value, bst.root.left_node))
print "--is root right subtree greater? "  + str(bst.isSubtreeGreater(bst.root.value,bst.root.right_node))
print "==is this a valid bst? " + str(bst.checkBST(bst.root))

print ""
print "-----delete fourteen----"
bst.deleteNode(None, bst.root, bst.fourteenNode)
bst.traverseBST(bst.root)
print ""
print "-----delete root----"
bst.deleteNode(None, bst.root, bst.root)
print "---traverse after delete---"
bst.traverseBST(bst.root)
print "--is root left subtree lesser? " + str(bst.isSubtreeLesser(bst.root.value, bst.root.left_node))
print "--is root right subtree greater? "  + str(bst.isSubtreeGreater(bst.root.value,bst.root.right_node))
print "==is this a valid bst? " + str(bst.checkBST(bst.root))
print ""
print "-----delete root again----"
bst.deleteNode(None, bst.root, bst.root)
print "---traverse after delete---"
bst.traverseBST(bst.root)
print "--is root left subtree lesser? " + str(bst.isSubtreeLesser(bst.root.value, bst.root.left_node))
print "--is root right subtree greater? "  + str(bst.isSubtreeGreater(bst.root.value,bst.root.right_node))
print "==is this a valid bst? " + str(bst.checkBST(bst.root))









