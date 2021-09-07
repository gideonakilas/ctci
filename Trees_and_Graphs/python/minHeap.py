from math import floor, isinf


class MinHeap:
    def __init__(self):
        self.heap = [float('-inf')]

    def add(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        self.heapifyUp(index)

    def heapifyUp(self, index: int):
        parent = floor(index / 2)

        if self.heap[index] <= 1:
            return

        if self.heap[parent] > self.heap[index]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            self.heapifyUp(parent)

    def pop(self):
        if len(self.heap) is 1:
            return
        small = self.heap[1]
        if len(self.heap) < 3:
            return self.heap.pop()
        self.heap[1] = self.heap.pop()
        if len(self.heap) < 4:
            return small
        else:
            self.heapifyDown(1)
        return small

    def heapifyDown(self, parent: int):
        left = (parent * 2)
        right = left + 1
        leftChild = self.indexCatch(left) or float('inf')
        rightChild = self.indexCatch(right) or float('inf')

        if isinf(leftChild) and isinf(rightChild):
            return

        if leftChild < rightChild:
            if self.heap[parent] > self.heap[left]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[left]
                self.heap[left] = temp
                self.heapifyDown(left)
        else:
            if self.heap[parent] > self.heap[right]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[right]
                self.heap[right] = temp
                self.heapifyDown(right)

    def indexCatch(self, index):
        try:
            return self.heap[index]
        except Exception as e:
            return None


minHeap = MinHeap()
minHeap.add(5)
minHeap.add(4)
minHeap.add(6)
minHeap.add(2)
minHeap.add(11)
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
minHeap.pop()
print(minHeap.heap)
