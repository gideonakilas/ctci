class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrderSuccessor(root: BinaryNode, node: BinaryNode):
    if root.val == node.val:
        return None
    successor = None
    while root:
        if root.val <= node.val:
            root = root.right
        elif root.val >= node.val:
            successor = root.val
            root = root.left
        else:
            break
    return successor


def example():
    root = BinaryNode(20)
    root.left = BinaryNode(8)
    root.right = BinaryNode(22)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(12)
    root.left.right.left = BinaryNode(10)
    root.left.right.right = BinaryNode(14)

    successor = inOrderSuccessor(root, root.left.right.left)
    print(successor)


if __name__ == "__main__":
    example()
