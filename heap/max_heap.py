

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.percolate_up(len(self.heap) - 1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):

        if len(self.heap) == 1:
            # if there is only one item in the heap, pop and return the item
            return self.heap.pop()
        elif len(self.heap) > 1:
            # if there are more than one items in the heap,
            # 1. save the first item
            # 2. move last item to a first
            # 3. delete last item
            # 4. heapify
            max_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heapify(0)
            return max_value

    def percolate_up(self, index):
        if index > 0:
            # find the parent of the last item that was inserted.

            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.percolate_up(parent)

    def heapify(self, index):
        # find left and right child
        left = (index * 2) + 1
        right = (index * 2) + 2

        # find the largest child and swap with it
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        # if largest is found and not the parent.
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)


max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(1)
print(max_heap.removeMax())
print(max_heap.removeMax())
print(max_heap.removeMax())
print(max_heap.removeMax())
