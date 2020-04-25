"""
You have to implement the minStack class which will have a min() function.
Whenever min() is called, the minimum value of the stack is returned in O(1) 
time. The element is not popped from the stack. Its value is simply returned.

Output #
Returns minimum number in O(1) time

Sample Output #
# minStack = [9, 3, 1, 4, 2, 5]
# minStack.min()
1
"""

# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()


class minStack:
    # Constructor
    def __init__(self):
        self.tempStack = myStack()
        self.myStack = myStack()

    # Removes and return value from newStack
    def pop(self):
        if self.myStack.isEmpty():
            return None
        item = self.myStack.pop()
        self.tempStack.pop()
        return item

    # Pushes values into newStack
    def push(self, value):
        if self.tempStack.isEmpty():
            self.tempStack.push(value)
        else:
            if self.tempStack.top() > value:
                self.tempStack.push(value)
            else:
                self.tempStack.push(self.tempStack.top())
        self.myStack.push(value)
        return True

# Returns minimum value from newStack in O(1) Time
    def min(self):
        return self.tempStack.top()

    # Write any helper functions here
