from collections import deque

from Linked_List.python.LinkedList import LinkedList


class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_node_list_by_depth(node: BinaryNode):
    queue = deque()
    queue.append(node)
    node_list = list()
    while len(queue) != 0:
        size = len(queue)
        ll = LinkedList()
        for i in range(size):
            node = queue.popleft()
            ll.node.next = LinkedList(node)
            ll.node = ll.node.next
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        node_list.append(ll.head.next)

    return node_list


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    print(levels)


if __name__ == "__main__":
    example()
