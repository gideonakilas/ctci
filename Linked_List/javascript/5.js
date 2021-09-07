const {LinkedList, Node} = require('./LinkedList');


var addTwoNumbers = function(l1, l2) {
    let node = new Node(0)
    let head = node
    let carry = 0;
    while(l1 != null || l2 != null){
        
        let val1 = l1 ? l1.val : 0;
        let val2 = l2 ? l2.val : 0;
        let sum = val1 + val2 + carry
        if(sum > 9){
            sum = sum % 10
            carry = 1
        } else{
            carry = 0;
        }
        node.next = new Node(sum)
        node = node.next
        if(l1) l1 = l1.next
        if(l2) l2 = l2.next
        }
    if (carry > 0){
        node.next = new Node(1)
    }
    return head.next

        
};


let l1 = new LinkedList(2)
let l2 = new LinkedList(2)
l1.add(1)
l1.add(1)
l1.add(3)
l2.add(5)
l2.add(5)
l2.add(6)
l2.add(7)

console.log(addTwoNumbers(l1.head, l2.head))