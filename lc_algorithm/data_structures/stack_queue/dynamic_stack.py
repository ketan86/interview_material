"""
Dynamic Stack, just like Dynamic Array, is a stack data structure whose the
length or capacity (maximum number of elements that can be stored) increases or
decreases in real time based on the operations (like insertion or deletion)
performed on it.

Stack is one of the most popular used data structure which has multiple
applications in real life. So we must be familiar with its structure and
implementation, so that we can use stack in our program with ease.


We know that stack could be implemented using array and such stack is known as
static stack but since we are using array to implement it we cannot insert
elements more than the size of array, it will show memory overflow because the
size of array is fixed. To overcome this drawback i.e to make stack dynamic we
implement stack using linkedlist and such stack is known as dynamic stack and in
this section we are going to learn dynamic stack.

Since we are using linkedlist to implement stack, lets get a brief idea about
structure of Linkedlist so that we can use it with more ease. Linkedlist
consists of consecutive linked nodes where each node consists of two parts data
part and address part, data part stores the value and address part contains the
address of next node. There is a pointer called head which stores the address of
first node and the address part of last node is set to null since it does not
point to any node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DynamicStack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            node = Node(data)
            node.next = curr
            self.head = node

    def pop(self):
        if not self.head:
            return
        curr = self.head
        self.head = curr.next
        return curr.data

    def peek(self):
        if not self.head:
            return
        return self.head.data

    def is_empty(self):
        if not self.head:
            return True
        return False

ds = DynamicStack()
ds.push(1)
ds.push(2)
ds.push(3)
ds.push(4)
print(ds.pop())
print(ds.pop())
print(ds.pop())
print(ds.pop())
print(ds.peek())
print(ds.is_empty())