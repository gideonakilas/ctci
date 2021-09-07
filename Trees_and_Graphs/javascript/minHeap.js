class MinHeap {

    constructor() {
        this.heap = [null]
    }
    add(val) {
        this.heap.push(val)
        if (this.heap.length > 2)
            this.heapifyUp(this.heap.length - 1)
    }
    pop() {
        if (this.heap.length < 2) return;
        else if(this.heap.length == 2){
            const smallest = this.heap.pop()
            return smallest
        } else if (this.heap.length == 3){
            const smallest = this.heap[1]
            this.heap[1] = this.heap.pop()
            return smallest
        }
         else {
            const smallest = this.heap[1]
            this.heap[1] = this.heap.pop()
            this.heapifyDown(1)
            return smallest
         }
    }

    heapifyUp(index) {
        if (index <= 1) return;
        let parent = Math.floor(index / 2)
        if (this.heap[parent] > this.heap[index]) {
            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]]
            this.heapifyUp(parent)
        }
    }

    heapifyDown(parent){
        const left = parent * 2
        const right = (parent * 2) + 1
        const leftChild = this.heap[left] || Infinity
        const rightChild = this.heap[right] || Infinity

        if (parent == this.heap.length-1 || this.heap[parent] == undefined) return;
        if(leftChild == Infinity && rightChild == Infinity) return;
        
        if (leftChild < rightChild){
            if(this.heap[parent] > this.heap[left]){
                [this.heap[parent], this.heap[left]] = [this.heap[left], this.heap[parent]]
                this.heapifyDown(left)
            } else if (this.heap[parent] > this.heap[right]){
                [this.heap[parent], this.heap[right]] = [this.heap[right], this.heap[parent]]
                this.heapifyDown(right)
        } else {
            if(this.heap[parent] > this.heap[right]){
                [this.heap[parent], this.heap[right]] = [this.heap[right], this.heap[parent]]
                this.heapifyDown(right)
            } else if (this.heap[parent] > this.heap[left]){
                [this.heap[parent], this.heap[left]] = [this.heap[left], this.heap[parent]]
                this.heapifyDown(left)
        }
        
}
        }
    
}
}
modules.export = MinHeap

let minHeap = new MinHeap()
minHeap.add(5)
minHeap.add(4)
minHeap.add(6)
minHeap.add(2)
minHeap.add(11)
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)
minHeap.pop()
console.log(minHeap.heap)