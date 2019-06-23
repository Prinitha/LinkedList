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

NodeObject1 = Node("Tuesday")
NodeObject2 = Node("Wedneday")
NodeObject3 = Node("Thursday")

HeadObject = Head()
HeadObject = NodeObject1

NodeObject1.address = NodeObject2
NodeObject2.address = NodeObject3

# print = Print_Node()

NodeToBeInserted = Node("Monday")
NodeToBeInserted.address = NodeObject1
HeadObject = NodeToBeInserted

print = Print_Node()