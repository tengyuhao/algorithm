"""
create a linked list
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node[{self.data}]"

    def __repr__(self):
        return f"Node[{self.data}]"


class SinglyLinkedList:
    def __init__(self):
        self.head = None


# test
# creating nodes
datalist = ['a', 'b', 'c', 'd', 'e']

mylinkedlist = SinglyLinkedList
lastNode = None

for i in range(len(datalist)):
    currentNode = Node(datalist[i])
    # print(currentNode)

    if i == 0:
        mylinkedlist.head = currentNode

    if lastNode is not None:
        lastNode.next = currentNode

    lastNode = currentNode


# print nodes
print(mylinkedlist.head)
print(mylinkedlist.head.next)
print(mylinkedlist.head.next.next)
print(mylinkedlist.head.next.next.next)
print(mylinkedlist.head.next.next.next.next)
