"""
Implement a function called sortStack() which takes a stack and sorts all of
its elements in ascending order such that when they are popped and printed,
they come out in ascending order. So the element that was pushed last to the
stack has to be the smallest.

Input #
A stack of integers.

Output #
The stack with all its elements sorted in descending order.

Sample Input #
stack = [23, 60, 12, 42, 4, 97, 2]
Sample Output #
result = [97, 60, 42, 23, 12, 4, 2]
# 2 was the value last pushed
"""
# pylint: skip-file
from stack import Stack


def sortStack(stack):
    # intialize the temp stack to store values in descending order
    # n....1
    tempStack = Stack()

    while not stack.isEmpty():
        curr = stack.pop()
        # if temp stack is empty, put the first value
        if tempStack.isEmpty():
            tempStack.push(curr)
        else:
            # if the curr value is greater than the top value of the tempstack,
            # put the curr value in the temp stack.
            if curr > tempStack.top():
                tempStack.push(curr)
            else:
                # if curr value is lower than the top value of the temp stack.
                # move all values from the temp stack to main stack.
                print([i for i in reversed(tempStack.stackList)])
                while not tempStack.isEmpty():
                    stack.push(tempStack.pop())
                tempStack.push(curr)

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())

    return stack


s = Stack()
s.push(2)
s.push(97)
s.push(4)
s.push(42)
s.push(12)
s.push(60)
s.push(23)

s = sortStack(s)
print(s.print())
