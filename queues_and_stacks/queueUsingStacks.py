import stack

stack1 = stack.stack()
stack2 = stack.stack()

def addElement(element):
    global stack1, stack2
    current = stack1.pop()
    while current!= None:
        stack2.push(current)
        current = stack1.pop()

    stack2.push(element)

def getNextElement():
    global stack1, stack2
    current = stack2.pop()
    while current!= None:
         stack1.push(current)
         current = stack2.pop()

    print "next element: " + str(stack1.pop())


addElement(1)
addElement(2)
addElement(3)
addElement(4)
getNextElement()
addElement(1)

getNextElement()
getNextElement()
getNextElement()
getNextElement()
