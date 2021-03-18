# pylint: skip-file

"""
Implement singly link list.

operations:
1. add(x) -> 0(1)
2. remove(x) -> 0(n)
3. len() -> 0(1)
4. search() -> 0(n)
5. contains() -> 0(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{0}->{1}'.format(self.data, self.next)


class SinglyLinkedList:
    def __init__(self):
        # pointer to head
        self.head = None
        # length of the ll
        self.length = 0

    def append(self, data):
        # copy head to avoid overwrite.
        node = self.head
        # if head is none, set head to new node
        if not node:
            self.head = Node(data)
        # else, loop until the the last node is found
        while node.next:
            node = node.next
        # set next node to new node
        node.next = Node(data)
        # increment the length
        self.length += 1

    def add(self, data):
        # add node to head
        node = Node(data)
        # move head to next node
        node.next = self.head
        # set new node to head
        self.head = node
        # increment the length
        self.length += 1

    def remove(self, data):
        # copy head to avoid overwrite
        node = self.head
        # if node is None, return
        if not node:
            return
        # prev pointer to attach prev node
        # to next node.
        prev = None
        # loop over all nodes
        while node:
            # if node is found
            if node.data == data:
                # if prev node is None, it's a head node
                # set head node to node.next (removes current
                # node). else it's middle or last node.
                # for both cases, prev.next = node.next will
                # detach the node.
                if not prev:
                    self.head = node.next
                else:
                    prev.next = node.next
                # break loop is node is removed.
                break
            # set prev node to current and current to next
            prev = node
            node = node.next

    def __len__(self):
        # return length
        return self.length

    def __contains__(self, data):
        # save the head
        node = self.head
        # loop until node is found or return False
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def __repr__(self):
        return '->'.join(self._iter_data())

    def _iter_data(self):
        # save the head node.
        node = self.head
        # loop and yield the node
        while node:
            yield str(node.data)
            node = node.next


s = SinglyLinkedList()
s.add(1)
s.remove(1)
print(s)
s.add(2)
s.add(3)
s.add(4)
# s.append(6)
# print(s)
# print(len(s))
s.remove(3)
# print(s)
# s.remove(1)
# print(len(s))
s.add(5)
s.add(10)
# s.remove(5)
# print(5 in s)
# print(len(s))
# print(s)
