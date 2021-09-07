class Node:
    def __init__(self, value, left=None, right=None):
        self.parent = None
        self.left = left
        self.right = right
        self.val = value


COUNT = [10]


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node = None

    @staticmethod
    def printBinaryTree(root, space, height):

        # Base case
        if root is None:
            return

        # increase distance between levels
        space += height

        # print right child first
        BinarySearchTree.printBinaryTree(root.right, space, height)
        print()

        # print the current node after padding with spaces
        for i in range(height, space):
            print(' ', end='')

        print(root.val, end='')

        # print left child
        print()
        BinarySearchTree.printBinaryTree(root.left, space, height)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return
        curr = self.root

        self.addNodeToTree(curr, val)
        print(self.root)

    def addNodeToTree(self, node: Node, val):
        if not node:
            return Node(val)

        if val < node.val:
            node.left = self.addNodeToTree(node.left, val)
        if val >= node.val:
            node.right = self.addNodeToTree(node.right, val)

        return node



bst = BinarySearchTree()
bst.insert(12)
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.insert(18)
bst.insert(13)
print(bst.printBinaryTree(bst.root, 0, 10))
