const {LinkedList} = require('./LinkedList');


LinkedList.prototype.removeDups = function (ll) {
    curr = ll.head
    set = new Set([curr.val])

    while(curr.next != null){
        if(set.has(curr.next.val)){
            curr.next = curr.next.next
        } else {
            if(curr.next != null){
                set.add(curr.next.val)
            }
            curr = curr.next
    
        }
    }
    return ll.head

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

ll.removeDups(ll)