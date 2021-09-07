class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node

    def add(self, value):
        node = Node(value)
        self.node.next = node
        self.node = self.node.next


ll = LinkedList(12)
ll.add(13)
ll.add(14)
ll.add(13)
ll.add(14)
