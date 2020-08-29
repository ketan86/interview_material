# pylint: skip-file
"""

- ith node, 2*i + 1 (left) 2*i + 2 (right)

1 4 7 4 5 7 9
    
          1

    4           7

4       5    7       9

[1, 4, 7, 4, 5, 7, 9]
 0  1  2  3  4  5  6  7

i = 2, 
    2*2 + 1 = 5th node left child   -> 7
    2*2 + 2 = 6th node right child -> 9

"""


class MinHeap:
    def __init__(self):
        # heap list to store the items
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        # percolate the item up to it's proper position
        self.percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]

    def remove_min(self):
        if len(self.heap) == 1:
            # if there is only one item in the heap, pop and return the item
            return self.heap.pop()
        elif len(self.heap) > 1:
            # if there are more than one items in the heap,
            # 1. save the first item
            # 2. move last item to a first
            # 3. delete last item
            # 4. heapify
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heapify(0)
            return min_value

    def percolate_up(self, index):
        if index > 0:
            # find the parent of the last item that was inserted.
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.percolate_up(parent)

    def heapify(self, index):
        # find left and right child
        left = (index * 2) + 1
        right = (index * 2) + 2

        # find the smallest child and swap with it
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        # if smallest is found and not the parent.
        if smallest != index:
            # swap the node values
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # heapify the smallest element.
            self.heapify(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__minHeapify(i)


min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(6)
min_heap.insert(2)
min_heap.insert(1)
import pdb
pdb.set_trace()
print(min_heap.remove_min())
print(min_heap.remove_min())
print(min_heap.remove_min())
print(min_heap.remove_min())
