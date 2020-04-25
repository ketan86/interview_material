# pylint: skip-file


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return '{0}->{1}'.format(self.data, self.next)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, data):
        new_node = Node(data)
        curr_node = self.head
        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        new_node.next = self.head
        curr_node.prev = new_node
        self.head = new_node
        self.length += 1

    def append(self, data):
        curr_node = self.head
        if curr_node is None:
            self.head = Node(data)
            self.length += 1
            return

        while curr_node.next is not None:
            curr_node = curr_node.next

        new_node = Node(data)
        curr_node.next = new_node
        new_node.prev = curr_node
        self.length += 1

    def remove(self, data):
        curr_node = self.head

        if curr_node is None:
            return

        if curr_node.data == data:
            self.head = curr_node.next
            self.length -= 1
            return

        while curr_node.next is not None:
            if curr_node.data == data:
                curr_node.next.prev = curr_node.prev
                curr_node.prev.next = curr_node.next
                self.length -= 1
            curr_node = curr_node.next

        if curr_node.data == data:
            curr_node.prev.next = None
            self.length -= 1

    def __contains__(self, data):
        curr_node = self.head
        if curr_node is None:
            return False

        if curr_node.data == data:
            return True

        while curr_node.next is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next

        if curr_node.data == data:
            return True

        return False

    def __repr__(self):
        return '->'.join(self._iter_data())

    def _iter_data(self):
        curr_node = self.head
        if curr_node is not None:
            yield str(curr_node.data)
        while curr_node.next is not None:
            yield str(curr_node.next.data)
            curr_node = curr_node.next


s = DoublyLinkedList()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(len(s))
s.append(4)
s.add(5)
# s.add(0)
s.append(0)
print(s)
s.remove(0)
s.remove(4)
print(len(s))
s.remove(1)
s.remove(2)
s.remove(3)
s.add(10)
print(len(s))
s.append(9)
s.remove(9)
print(0 in s)
print(s)
print(len(s))
