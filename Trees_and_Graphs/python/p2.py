from math import floor

head = None
class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    @staticmethod
    def printBinaryTree(root, space, height):

        # Base case
        if root is None:
            return

        # increase distance between levels
        space += height

        # print right child first
        Node.printBinaryTree(root.right, space, height)
        print()

        # print the current node after padding with spaces
        for i in range(height, space):
            print(' ', end='')

        print(root.val, end='')

        # print left child
        print()
        Node.printBinaryTree(root.left, space, height)




def makeBinaryTree(array, start, end):
    if start > end:
        return None
    mid = floor((start + end) / 2)
    root = Node(array[mid])
    root.left = makeBinaryTree(array, start,  mid-1)
    root.right = makeBinaryTree(array, mid+1, end)

    return root


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    node = Node(test_array[0])
    root = makeBinaryTree(test_array, 0, len(test_array) - 1)
    print(node.printBinaryTree(root, 0, 10))
