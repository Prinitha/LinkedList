class Node:
    def __init__(self, data):
        self.data = data
        self.address = None

class Head:
    def __init__(self):
        self.head = None

    def PrintNodes(self):
        printPointer = head
        while printPointer is not None:
            print(printPointer.data)
            printPointer = printPointer.address

    def NodeToBeDeleted(self):
        deletePointer = head
        previousPointer = deletePointer
        while deletePointer is not None:
            if deletePointer.data == NodeValueToBeDeleted:
                if previousPointer == deletePointer:
                    deletePointer = deletePointer.address
                previousPointer.address = deletePointer.address
            previousPointer = deletePointer
            deletePointer = deletePointer.address




NodeObject1 = Node("Monday")
NodeObject2 = Node("Tuesday")
NodeObject3 = Node("Wednesday")
NodeObject4 = Node("Thursday")
NodeObject5 = Node("Friday")

head = Head()
myObject = Head()
head = NodeObject1

NodeObject1.address = NodeObject2
NodeObject2.address = NodeObject3
NodeObject3.address = NodeObject4
NodeObject4.address = NodeObject5

myObject.PrintNodes()

NodeValueToBeDeleted = input("Please enter the value that you need to delete?")

myObject.NodeToBeDeleted()
myObject.PrintNodes()
