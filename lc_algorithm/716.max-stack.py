# Design a max stack data structure that supports the stack operations and
# supports finding the stack's maximum element.

# Implement the MaxStack class:

# MaxStack() Initializes the stack object. void push(int value) Pushes element value
# onto the stack. int pop() Removes the element on top of the stack and returns
# it. int top() Gets the element on the top of the stack without removing it.
# int peekMax() Retrieves the maximum element in the stack without removing it.
# int popMax() Retrieves the maximum element in the stack and removes it. If
# there is more than one maximum element, only remove the top-most one.

# Example 1:

# Input
# ["MaxStack", "push", "push", "push", "top",
#     "popMax", "top", "peekMax", "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# Output
# [null, null, null, null, 5, 5, 1, 5, 1, 5]

# Explanation
# MaxStack stk = new MaxStack()
# stk.push(5)
# // [5] the top of the stack and the maximum number is 5.
# stk.push(1)
# // [5, 1] the top of the stack is 1, but the maximum is 5.
# stk.push(5)
# // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
# stk.top()
# // return 5, [5, 1, 5] the stack did not change.
# stk.popMax()
# // return 5, [5, 1] the stack is changed now, and the top is different from the max.
# stk.top()
# // return 1, [5, 1] the stack did not change.
# stk.peekMax()
# // return 5, [5, 1] the stack did not change.
# stk.pop()
# // return 1, [5] the top of the stack and the max element is now 5.
# stk.top()
# // return 5, [5] the stack did not change.


# Constraints:

# -107 <= value <= 107
# At most 104 calls will be made to push, pop, top, peekMax, and popMax.
# There will be at least one element in the stack when pop, top, peekMax, or popMax is called.


# Follow up: Could you come up with a solution that supports O(1) for each top
# call and O(logn) for each other call?


from collections import OrderedDict
import heapq


class MaxStack:
    """Doubly linked list as stack and Map <-> DLL Node mapping

    Let's store the stack as a double linked list dll, and store a map 
    from value to a List of Node.

    When we MaxStack.push(value), we add a node to our dll, and add or update 
    our entry map.get(value).add(node).

    When we MaxStack.pop(), we find the value val = dll.pop(), and remove 
    the node from our map, deleting the entry if it was the last one.

    When we MaxStack.popMax(), we use the map to find the relevant node to 
    unlink, and return it's value.

    Time -> O(1) for popMax() and O(log n) for others
    Space -> O(n)
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.index = 0
        # heap to maintain max element at top for max pop.
        self.max_heap = []            # priority queue
        # ordered map to insert/pop items in order
        # NOTE: There is no key and there can be duplicate so use index
        # as key to store multiple same values.
        self.map = OrderedDict()  # ordered dict

    def push(self, value: int) -> None:
        # push to max heap and update the map with index starting from 0 and
        # decreasing it.
        heapq.heappush(self.max_heap, (-value, self.index))
        self.map[self.index] = value
        # when value is same in heap, we want to latest one stays on top so
        # use index in reverse order.
        self.index -= 1

    def pop(self) -> int:
        # we do not update max heap here but instead during peekmax.
        index, value = self.map.popitem(last=True)
        return value

    def top(self) -> int:
        index, value = self.map.popitem(last=True)
        # put popped value back to map
        self.map[index] = value
        return value

    def peekMax(self) -> int:
        # remove all entries we did not during the pop operation from max_heap.
        while self.max_heap:
            value, index = heapq.heappop(self.max_heap)
            if index in self.map:
                break
        # put value back
        heapq.heappush(self.max_heap, (value, index))
        return -value

    def popMax(self) -> int:
        # pop keys that are removed from the map during pop() but not from the
        # heap.
        while self.max_heap:
            value, index = heapq.heappop(self.max_heap)
            if index in self.map:
                break
        # pop value that we wanted remove
        self.map.pop(index)
        return -value


class MaxStack:
    """
    Time -> O(n) for popMax() and O(1) for others
    Space -> O(n)
    Runtime: 148 ms, faster than 73.95%

    Considering list <-> singly linked list
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        # stores element and max so far
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            # current element and max(current, prev_max)
            self.stack.append((value, max(self.stack[-1][1], value)))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        mx = self.peekMax()

        temp_stack = []
        # find the max
        while self.stack[-1][0] != mx:
            temp_stack.append(self.stack.pop())

        # pop max
        self.pop()

        # put elements back to main stack while calculating the max
        while temp_stack:
            value, mx = temp_stack.pop()
            if self.stack:
                self.stack.append((value, max(value, self.stack[-1][1])))
            else:
                self.stack.append((value, value))

        return mx

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(value)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
