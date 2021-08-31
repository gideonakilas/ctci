const {LinkedList, Node} = require('./LinkedList');


LinkedList.prototype.removeKthLastElement = function (ll, k) {
    let dummyHead = new Node(null, ll.head)
    slow = dummyHead
    fast = dummyHead

    for(let i=0; i< k; i++)
        fast = fast.next;
    
    
    while(fast.next != null){
            slow = slow.next
            fast = fast.next
    }
    slow.next = slow.next.next
    return dummyHead.next

};

let ll = new LinkedList(12)
ll.add(13)
ll.add(13)
ll.add(14)
ll.add(15)
ll.add(15)
ll.add(16)
ll.add(17)
ll.add(17)

ll.removeKthLastElement(ll, 4)