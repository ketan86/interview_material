"""
Implement the function reverseK(queue, k) which takes a queue and a number
“k” as input and reverses the first “k” elements of the queue.
An illustration is also provided for your understanding.

Output #
The queue with first “k” elements reversed. Remember to return the queue itself!

In case the value of “k” is larger than the size of the queue, is smaller
than 0, or if the queue is empty, simply return None instead.

Sample Input #
Queue = [1,2,3,4,5,6,7,8,9,10], k = 5
Sample Output #
Queue = [5,4,3,2,1,6,7,8,9,10]

"""
from my_queue import Queue
from stack import Stack


def reverseK(queue, k):
    if queue.isEmpty() or queue.size() < k or k < 0:
        return None

    result_queue = Queue()
    temp_stack = Stack()

    while not queue.isEmpty():
        if temp_stack.size() == k:
            break
        temp_stack.push(queue.dequeue())

    while not temp_stack.isEmpty():
        result_queue.enqueue(temp_stack.pop())

    while not queue.isEmpty():
        result_queue.enqueue(queue.dequeue())

    return result_queue


# without using another queue

def reverseK(queue, k):
    # if queue is empty or size is less than k or k < 0,
    # return none
    if queue.isEmpty() or queue.size() < k or k < 0:
        return None

    # use temp stack to store the first k elements
    # so while poping, it can be reversed
    temp_stack = Stack()

    # dequeue k elements and push it to temp stack
    for i in range(k):
        temp_stack.push(queue.dequeue())

    # pop k elements and enqueue them to main stack
    while not temp_stack.isEmpty():
        queue.enqueue(temp_stack.pop())

    # dequeue remaining elements from the main stack
    # and enqueue them back one by one.
    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue


q = Queue()
q.enqueue(2)
q.enqueue(6)
q.enqueue(3)
q.enqueue(8)
q.enqueue(5)
q.enqueue(1)
q.enqueue(0)
q = reverseK(q, 3)
print(q)
