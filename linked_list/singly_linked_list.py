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
        self.head = None
        self.length = 0

    def append(self, data):
        node = self.head
        if node is None:
            self.head = Node(data)
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        self.length += 1

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def remove(self, data):
        node = self.head
        if node is None:
            return
        if node is not None:
            if node.data == data:
                self.head = node.next
                return
        while node is not None:
            if node.data == data:
                break
            prev = node
            node = node.next
        prev.next = node.next
        node = None

    def __len__(self):
        return self.length

    def __contains__(self, data):
        node = self.head
        if node.data == data:
            return True
        while node.next is not None:
            if node.data == data:
                return True
            node = node.next
        return False

    def __repr__(self):
        return '->'.join(self._iter_data())

    def _iter_data(self):
        node = self.head
        if node is not None:
            yield str(node.data)
        while node.next is not None:
            yield str(node.next.data)
            node = node.next


s = SinglyLinkedList()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.append(6)
print(s)
print(len(s))
s.remove(4)
s.remove(1)
print(len(s))
s.add(5)
s.add(10)
s.remove(5)
print(5 in s)
print(len(s))
print(s)
