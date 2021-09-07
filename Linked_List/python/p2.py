from LinkedList import LinkedList


def kthLastElement(ll, k):
    fast = ll.head
    slow = ll.head
    while fast.next is not None and k > 0:
        fast = fast.next
        k -= 1
    if k > 0:
        return None
    while fast is not None:
        fast = fast.next
        slow = slow.next

    return slow.val


# 12->13->14->15->None


ll = LinkedList(12)
ll.add(13)
ll.add(13)
ll.add(14)
ll.add(15)
ll.add(15)
ll.add(16)
ll.add(17)
ll.add(17)

kthLastElement(ll, 14)
