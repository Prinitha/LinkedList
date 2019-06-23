# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
# # Function to add node
#     def Inbetween(self, middle_node, newdata):
#         print(middle_node.dataval)
#         if middle_node is None:
#             print("The mentioned node is absent")
#             return
#
#         NewNode = Node(newdata)
#         NewNode.nextval = middle_node.nextval
#         middle_node.nextval = NewNode
#
# # Print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval
#
#
# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Thu")
#
# list.headval.nextval = e2
# e2.nextval = e3
# print("BEFORE")
# list.listprint()
#
# list.Inbetween(list.headval.nextval, "Fri")
#
# print("AFTER")
# list.listprint()



class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, printval.nextval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()