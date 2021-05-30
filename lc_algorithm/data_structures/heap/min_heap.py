# pylint: skip-file
"""
NOTE: A Min Heap is a Complete Binary Tree. It should be filled from left to
right where right elements can be right nodes can be left empty.

A Min heap is typically represented
as an array. The root element will be at Arr[0]. For any ith node, i.e.,
Arr[i]:
    Arr[(i -1) / 2] returns its parent node.
    Arr[(2 * i) + 1] returns its left child node.
    Arr[(2 * i) + 2] returns its right child node.



- ith node, 2*i + 1 (left) 2*i + 2 (right)

    1 4 7 4 5 7 9

          1

    4           7

4       5    7       9

heap -> [1, 4, 7, 4, 5, 7, 9] index -> 0  1  2  3  4  5  6

for index i = 2, 2*2 + 1 = 5th node left child   -> 7 2*2 + 2 = 6th node right
    child -> 9
...

Operations on Min Heap :

get_min(): It returns the root element of Min Heap. Time Complexity of this
operation is O(1).

remove_min(): Removes the minimum element from MinHeap. Time Complexity of this
Operation is O(Log n) as this operation needs to maintain the heap property (by
calling heapify()) after removing root.

insert(): Inserting a new key takes O(Log n) time. We add a new key at the end
of the tree. If new key is larger than its parent, then we don’t need to do
anything. Otherwise, we need to traverse up to fix the violated heap property.
"""


class MinHeap:
    def __init__(self):
        # heap list to store the items
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        # traverse the item up to it's proper position
        self.traverse_up(len(self.heap) - 1)

    def get_min(self):
        # if heap is not empty, return the first value
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

    def traverse_up(self, index):
        # only balance if index is greater than 0
        if index > 0:
            # find the parent of the last item that was inserted.
            # keep swapping with parent until parent is less than
            # the newly added element.
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.traverse_up(parent)

    def heapify(self, index):
        # find left and right child
        left = (index * 2) + 1
        right = (index * 2) + 2

        # compare the child of the index element and find the min of
        # the child and if that is less than the index element, swap

        # in order to find smallest, we have to take two step approach
        # because either left or right or both can be None.
        # 1. we set smallest to node that is being swapped
        # 2. if left node is there and it's smaller than current node,
        # make left a smallest
        # 3. if right node is there and it's smaller than smallest so far,
        # make right a smallest.
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right

        # if smallest is found and not the parent. this is similar to
        # comapring if parent is less than the smallest.
        if smallest != index:
            # swap the node values
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # heapify the smallest element.
            self.heapify(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.heapify(i)


min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(6)
min_heap.insert(2)
min_heap.insert(1)
print(min_heap.remove_min())
print(min_heap.remove_min())
print(min_heap.remove_min())
print(min_heap.remove_min())
