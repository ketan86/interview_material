"""
Implement stack and Queue using the Stack.
"""
# pylint:skip-file

class Stack:
    def __init__(self):
        # use list to implement stack. 
        # most preferable is a linked list with head and tail pointer.
        self.stack = []

    def peek(self):
        # if stack is not empty, return last item without poping
        if not self.is_empty():
            return self.stack[-1]

    def pop(self):
        # if stack is not empty, pop top item and return 
        if not self.is_empty():
            return self.stack.pop()

    def push(self, value):
        # add item to top of the stack
        return self.stack.append(value)

    def is_empty(self):
        # return True if stack is empty else False
        return len(self.stack) == 0

    def __len__(self):
        # length of the stack.
        return len(self.stack)



class Queue:
    """
    To implement queue using stack, we need two stacks and based on the
    requirement of the algorithm, either `enqueue` or `dequeue` can be
    optimized for better performance. 

    for ex, 
        1. during  `enqueue` operation, move all items from main stack to 
        temp stack. add new item in the main stack and then move all items
        back from the temp stack to main stack.

        since we add item to bottom of the stack, pulling item from the
        top of the stack is efficient during the `dequeue`. 

        or 

        2. during `dequque` operation, move all items from the main stack
        to temp stack, pop item from the temp stack (dequeue item) and
        return rest of the item back to main stack.  

        we add item to the top of the stack during `enqueue` operation.
    """
    def __init__(self):
        # To implement queue using stack, we need two stacks.
        self.main_stack = Stack()
        self.temp_stack = Stack()
        # save top item to make peek efficient.
        self.top_item = None 

    def enqueue(self, value):
        # if main stack is empty, store the top item for peeking 
        if self.main_stack.is_empty():
            self.top_item = value
        # push item to main stack
        self.main_stack.push(value)

    def dequeue(self):
        # move all items to temp stack, pop item from the temp and move
        # rest to main stack.
        while not self.main_stack.is_empty():
            item = self.main_stack.pop()
            self.temp_stack.push(item)

        dequeue_item = self.temp_stack.pop()
        
        # if temp stack is empty after the dequeue, set top item to none
        if self.temp_stack.is_empty():
            self.top_item = None
        # else, next temp item becomes the first item.
        else:
            self.top_item = self.temp_stack.peek()

        # move all items from temp to main stack
        while not self.temp_stack.is_empty():
            item = self.temp_stack.pop()
            self.main_stack.push(item)
        
        return dequeue_item

    def peek(self):
        # return the item that will be dequeued
        return self.top_item

    def is_empty(self):
        # return if queue is empty or not
        return self.main_stack.is_empty()

    def __len__(self):
        # size of the queue
        return len(self.main_stack)



# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
