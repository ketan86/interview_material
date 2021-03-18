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
# pylint:skip-file

# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()
from stack import Stack


class MinStack:
    """Use a temp stack to store the min value so far when elements
    are pushed to the stack. When min value of the stack is requested,
    return the top value of the temp stack. When item is removed from
    the main stack, pop the temp stack value too."""

    # Constructor
    def __init__(self):
        # temp stack to store the min value after new
        # element is push to the main stack.
        self.tempStack = Stack()
        self.myStack = Stack()

    # Removes and return value from newStack
    def pop(self):
        # if main stack is empty, return None
        if self.myStack.isEmpty():
            return None
        # pop the item from the main stack.
        item = self.myStack.pop()
        # pop the min value of the main stack
        # from the temp stack.
        self.tempStack.pop()
        return item

    # Pushes values into newStack
    def push(self, value):
        # If temp stack is empty, value is min so far
        # push it to temp and main stack.
        if self.tempStack.isEmpty():
            self.tempStack.push(value)
        else:
            # find the min and push it to temp stack.
            self.tempStack.push(min(value, self.tempStack.top()))
        self.myStack.push(value)
        return True

    # Returns minimum value from newStack in O(1) Time
    def min(self):
        # return the top min value of the temp stack
        return self.tempStack.top()


s = MinStack()
s.push(2)
s.push(3)
s.push(1)
s.push(6)
s.push(12)
# s.push(0)
print(s.min())
s.pop()
s.pop()
s.pop()
print(s.min())
