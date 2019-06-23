# Creation of a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.address = None


class Pointer_Head:
    def __init__(self):
        self.head = None

class Print_Nodes:
    def __init__(self):
        print_object = header
        while print_object is not None:
            print(print_object.data, print_object)
            print_object = print_object.address



node_object0 = Node("Monday")
node_object1 = Node("Tuesday")
node_object2 = Node("Thursday")

header = Pointer_Head()
header = node_object0

node_object0.address = node_object1
node_object1.address = node_object2

print_object = Print_Nodes()


