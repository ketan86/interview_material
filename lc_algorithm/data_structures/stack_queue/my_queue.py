class Queue:
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
    
    """
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return self.size() == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front

    def __repr__(self):
        return str(self.queueList)
