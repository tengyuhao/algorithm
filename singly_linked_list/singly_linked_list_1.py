
"""
create a linked list
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:

    def __init__(self):
        self.head = None


# test
# creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# link
node1.next = node2
node2.next = node3
print(type(node1.next))
print(type(node2.next))


mylinkedlist = SinglyLinkedList()
mylinkedlist.head = node1

print(mylinkedlist.head.data)
print(mylinkedlist.head.next.data)
print(mylinkedlist.head.next.next.data)