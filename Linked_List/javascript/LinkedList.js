class Node {
    constructor(val = null, next = null){
        this.val = val
        this.next = next
    }
}
class LinkedList {
    constructor(val = null){
        this.node = new Node(val)
        this.head = this.node
        this.length = 1
    }

    add(val){
        let node = new Node(val)
        this.node.next = node
        this.node = this.node.next
        this.length++;
    }

    delete(val){
        let curr = this.head
        if (curr.val == val){
            this.head = this.head.next
        }
        while(curr.next != null){
            if(curr.next.val == val){
                curr.next = curr.next.next
            }
            curr = curr.next
        }
        this.node = curr
        this.length--;
    }
}

module.exports = {LinkedList, Node}

// let ll = new LinkedList(12)
// ll.add(13)
// ll.add(13)
// ll.add(14)
// ll.delete(13)
// ll.add(14)
// console.log(ll.val)


