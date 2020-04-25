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


def sortStack(stack):
    tempStack = myStack()

    while not stack.isEmpty():
        curr = stack.pop()
        if tempStack.isEmpty():
            tempStack.push(curr)
        else:
            while not tempStack.isEmpty():
                item = tempStack.pop()
                if curr >= item:
                    tempStack.push(item)
                    tempStack.push(curr)
                    break
                else:
                    stack.push(item)
            else:
                tempStack.push(curr)

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())

    return stack
