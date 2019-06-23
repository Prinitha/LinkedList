class Node:
    def __init__(self, data):
        self.data = data
        self.address = None

class Head:
    def __init__(self):
        self.head = None

    def insertionAtTheEnd(self):
        firstObject = headPointer
        while firstObject is not None:
            if firstObject.address is None:
                firstObject.address = newNodeToBeInserted
                newNodeToBeInserted.address = None
            firstObject = firstObject.address

    def printList(self):
        firstObject = headPointer
        while firstObject is not None:
            print(firstObject.data)
            firstObject = firstObject.address


firstObject = Node("Monday")
secondObject = Node("Tuesday")
thirdObject = Node("Wednesday")
fourthObject = Node("Thursday")

headPointer = Head()
pointObject = Head()
headPointer = firstObject

firstObject.address = secondObject
secondObject.address = thirdObject
thirdObject.address = fourthObject

newNodeToBeInserted = Node(input("Please insert \nThe value of the node to "
                                 "be inserted at the end: "))

pointObject.insertionAtTheEnd()
pointObject.printList()

