const {LinkedList} = require('./LinkedList');


LinkedList.prototype.deleteCurrNode = function (node) {
        node.val = node.next.val;
        node.next = node.next.next;
        return ll.head
};

let ll = new LinkedList(12)
ll.add(13)
ll.add(13)
ll.add(14)
let node = ll.node
ll.add(15)
ll.add(15)
ll.add(16)
ll.add(17)
ll.add(17)

ll.deleteCurrNode(node)