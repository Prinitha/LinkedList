class Node:
    def __init__(self, data):
        self.data = data
        self.address = None

class Head:
    def __init__(self):
        self.head = None

    def Print(self):
        printvalue = self.head
        while(printvalue is not None):
            print(printvalue.data)
            printvalue = printvalue.address

    def reverse(self):
        print("Entered")
        prevElement = None
        nextElement = None
        curr = self.head
        # print(curr.data)
        while curr is not None:
            nextElement = curr.address
            curr.address = prevElement
            # print(curr.data)
            prevElement = curr
            curr = nextElement
        self.head = prevElement

mainhead = Head()
mainhead.head = Node("1")
NodeObject1 = mainhead.head
NodeObject2 = Node("2")
NodeObject3 = Node("3")
NodeObject4 = Node("4")
NodeObject5 = Node("5")

NodeObject1.address = NodeObject2
NodeObject2.address = NodeObject3
NodeObject3.address = NodeObject4
NodeObject4.address = NodeObject5

mainhead.Print()
mainhead.reverse()
mainhead.Print()



