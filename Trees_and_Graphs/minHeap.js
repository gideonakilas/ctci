class MinHeap {

    constructor() {
        this.heap = [null]
    }
    add(val) {
        this.heap.push(val)
        if (this.heap.length > 2)
            this.heapify(this.heap.length - 1)
    }
    pop() {
        if (this.heap.length < 2) return;
        else if(this.heap.length == 2){
            const value = this.heap.pop()
            return value
        } else if (this.heap.length == 3){
            const smallest = this.heap[0]
            this.heap[0] = this.heap.pop()
            return smallest
        }
         else {
            const smallest = this.heap[0]
            this.heap[0] = this.heap.pop()
            this.heapifyDown()
            return smallest
         }
        if (this.heap.length > 2)
            this.heapifyUp(this.heap.length - 1)
    }
    heapifyUp(index) {
        if (index <= 1) return;
        let parent = Math.floor(index / 2)
        if (this.heap[parent] > this.heap[index]) {
            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]]
            this.heapifyUp(parent)
        }
    }

    heapifyDown(index = 1){
        const parent = Math.floor(index /2)
        const left = Math.floor(index /2)

    }
}

let minHeap = new MinHeap()
minHeap.add(5)
minHeap.add(4)
minHeap.add(6)
minHeap.add(2)
minHeap.add(11)
console.log(minHeap.heap)