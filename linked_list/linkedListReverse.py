import stack

class linkedList:
    nextNode = None
    value = None
    def __init__(self, value=0, nextNode = None):
        self.nextNode = nextNode
        self.value = value

node7 = linkedList(120, None)
node6 = linkedList(50, node7)
node5 = linkedList(25, node6)
node4 = linkedList(200, node5)
node3 = linkedList(204, node4)
node2 = linkedList(130, node3)
node1 = linkedList(300, node2)

head = node1

def traverseForward(head):
    node = head
    print node.value
    while node.nextNode!=None:
        node = node.nextNode
        print node.value

def reverseList(headIn):
    prev = None
    current = headIn
    nextNode = current.nextNode
    while current!=None:
        temp = current
        current = current.nextNode
        temp.nextNode = prev
        prev = temp
    return temp

def traverseReverseWithStack(head):
    current = head
    stackTest = stack.stack()
    while current!=None:
        stackTest.push(current)
        current = current.nextNode

    currentPop = stackTest.pop()
    while currentPop!=None:
        print currentPop.value
        currentPop = stackTest.pop()


def reverseLinkedListRecursive(prev, node):
    if node.nextNode == None:
        node.nextNode = prev
        return node
    head = reverseLinkedListRecursive(node,node.nextNode)
    node.nextNode = prev
    return head


print "------traverseForward-----"
traverseForward(head)

print "-----traverseReverseWithStack------"
traverseReverseWithStack(head)

print "------reverseList----"
head = reverseList(head)
print "------traverseReverseWithStack------"
traverseReverseWithStack(head)
print "------reverseRecursive------"
head = reverseLinkedListRecursive(None, head)
print "------traverseForward-----"
traverseForward(head)
print "-------end program-----"
