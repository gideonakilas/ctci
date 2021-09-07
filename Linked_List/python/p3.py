from LinkedList import LinkedList


def deleteMiddleNode(node):
    node.val = node.next.val
    node.next = node.next.next
    return node


# 12->13->14->15->None


ll = LinkedList(12)
ll.add(13)
ll.add(13)
ll.add(14)
node = ll.node
ll.add(15)
ll.add(15)
ll.add(16)
ll.add(17)
ll.add(17)
deleteMiddleNode(node)


