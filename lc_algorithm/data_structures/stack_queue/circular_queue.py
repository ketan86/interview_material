"""
Circular queue avoids the wastage of space in a regular queue implementation
using arrays.
"""
class Full(Exception):
    """Queue full exception"""

class Empty(Exception):
    """Queue empty exception"""

class CircularQueue:
    """
    Queue using Arrays and fixed size would not allow insertion of new
    items at the end until all items are dequeued. for ex,
        queue size => 5
        0 1 2 3 4
       [x x x x x]
                         0 1 2 3 4
                        [x x x x x]
       enqueue -> 1     [1 x x x x]
       enqueue -> 2     [1 2 x x x]
       enqueue -> 3     [1 2 3 x x]
       enqueue -> 4     [1 2 3 4 x]
       enqueue -> 5     [1 2 3 4 5]

       dequeue -> 1     [x 2 3 4 5]
                           ^     ^
                           f     r
       is_full -> True because the rear is pointing to last element even
                  though first element in the array is empty.

    Usually, queue is implemented using linked list to avoid this problem but
    if constraint is to implement the the queue using array and fixed size.
    Queue can also be implemented using using the fixed size linked list and
    using it in the circular manner.

    Circular queue can be implemented using array to overcome the above problem
    by moving the rear pointer(circular) manner to allow enqueuing items.
    
        queue size => 5
        0 1 2 3 4
       [x x x x x]
                      -1 0 1 2 3 4
                        [x x x x x]
                       h
                       t
       enqueue -> 1     [1 x x x x]
                         h
                         t
       enqueue -> 2     [1 2 x x x]
                         h t
       enqueue -> 3     [1 2 3 x x]
       enqueue -> 4     [1 2 3 4 x]
       enqueue -> 5     [1 2 3 4 5]
                         h       t
       dequeue -> 1     [x 2 3 4 5]
                           ^     ^
                           h     t
       is_full -> False because a new element can be added in the head.

       enqueue -> 6     [6 2 3 4 5]
                         ^ ^
                         t h
    """
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.head = -1
        self.tail = -1

    def enqueue(self, data):
        # if both nodes are at -1, first element, so set head, tail and data
        # to/on 0'th index.
        if self.head == -1 and self.tail == -1:
            self.queue[0] = data
            self.head += 1
            self.tail += 1
            return

        # find the circular index for enqueue operation
        self.tail = (self.tail + 1) % self.size

        # if head and tail are at the same node, queue is considered full
        if self.head == self.tail:
            raise Full('Queue is full..')
        # else, set the data
        else:
            self.queue[self.tail] = data

    def dequeue(self):
        # if head and tail are at -1, queue is emptry
        if self.head == -1 and self.tail == -1:
            raise Empty('Queue is empty')

        # if head and tail are same, we are at the 0th index and return data
        # and set head and tail to -1
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        # else, copy the data at current node and move head to next index in
        # circular array.
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp


    def peak(self):
        # if head and tail are -1, queue us empty else, return latest element
        # at head
        if self.head == -1 and self.tail == -1:
            raise Empty('Queue is empty')
        return self.queue[self.head]

    def is_empty(self):
        # if head and tail are -1, queue is empty else not.
        if self.head == -1 and self.tail == -1:
            return True
        return False


cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
print(cq.queue)
# print(cq.is_empty())
# print(cq.peak())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
# print(cq.peak())ß
print(cq.is_empty())
cq.enqueue(3)
cq.enqueue(2)
print(cq.peak())
print(cq.is_empty())