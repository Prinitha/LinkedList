class Node:
    def __init__(self, data):
        self.data = data
        self.address = None

class Head:
    def __init__(self):
        self.head = None

class Print_Node:
    def __init__(self):
        print_Object = HeadObject
        while print_Object is not None:
            print(print_Object.data)
            print_Object = print_Object.address

class Middle:
    def __init__(self, node, target):
        # print("Entered", node.data)
        currentNode = NodeObject1
        while currentNode is not None:
            if(currentNode.data == target):
                previousNode = currentNode
                currentNode = previousNode.address
                node.address = currentNode
                previousNode.address = node
            currentNode = currentNode.address



NodeObject1 = Node("Monday")
NodeObject2 = Node("Tuesday")
NodeObject3 = Node("Thursday")

HeadObject = Head()
HeadObject = NodeObject1

NodeObject1.address = NodeObject2
NodeObject2.address = NodeObject3

# object = Print_Node()

NodeToBeInsertedBetween = Node("Wednesday")
MiddleObject = Middle(NodeToBeInsertedBetween, "Tuesday")

print = Print_Node()