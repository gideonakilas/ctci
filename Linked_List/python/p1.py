from LinkedList import LinkedList


def removeDups(ll):
    dupSet = set()
    curr = ll.head

    while curr.next is not None:
        if curr.next.val in dupSet:
            curr.next = curr.next.next
        else:
            curr = curr.next
            if curr.next:
                dupSet.add(curr.next.val)

    return ll.head


ll = LinkedList(12)
ll.add(13)
ll.add(13)
ll.add(14)
ll.add(15)
ll.add(15)
ll.add(16)
ll.add(17)
ll.add(17)

removeDups(ll)
