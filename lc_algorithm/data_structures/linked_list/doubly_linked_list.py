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
        # head pointer
        self.head = None
        # length of the ll
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, data):
        # create a node
        new_node = Node(data)
        # copy head node
        curr_node = self.head
        # attach new node next to head
        new_node.next = curr_node
        # if head node is not None.
        if curr_node:
            curr_node.prev = new_node
        # move head to new node
        self.head = new_node
        # increment the length
        self.length += 1

    def append(self, data):
        # copy head node
        curr_node = self.head

        # find the last node
        while curr_node.next:
            curr_node = curr_node.next

        # create a new node
        new_node = Node(data)
        # set current node's next to new node
        curr_node.next = new_node
        # set new node's prev to current node
        new_node.prev = curr_node
        # increment the length
        self.length += 1

    def remove(self, data):
        # copy head node
        curr_node = self.head

        # loop over the ll
        while curr_node:
            # if data is found
            if curr_node.data == data:
                # copy next and prev pointers
                next_ = curr_node.next
                prev = curr_node.prev
                # if prev is not None, it's
                # a middle node so set prev.next
                # to next node.
                # else, it's a head node so set
                # next node to head.
                if prev:
                    prev.next = next_
                else:
                    self.head = next_
                # if next_ is not None, it's
                # a middle node so set next.prev
                # to prev node.
                # NOTE: we do not have to handle the
                # tail node condition because if curr
                # node is a tail node, next_ node's
                # prev does not have to be attached
                # to prev node.
                if next_:
                    next_.prev = prev

                # decrement the length and break
                self.length -= 1
                break
            # go to next node
            curr_node = curr_node.next

    def __contains__(self, data):
        # copy head node
        curr_node = self.head

        # loop over the ll
        while curr_node:
            # if data is found, return True
            if curr_node.data == data:
                return True
            curr_node = curr_node.next

        return False

    def __repr__(self):
        return '->'.join(self._iter_data())

    def _iter_data(self):
        # copy head node
        curr_node = self.head
        # loop over the nodes
        while curr_node:
            # yield node
            yield str(curr_node.data)
            # move to next node
            curr_node = curr_node.next


s = DoublyLinkedList()
s.add(1)
s.add(2)
s.add(3)
# print(s)
s.append(4)
s.add(5)
s.append(0)
s.add(0)
print(s)
s.remove(0)
s.remove(4)
print(s)
# print(len(s))
# s.remove(1)
# s.remove(2)
# s.remove(3)
# s.add(10)
# print(len(s))
# s.append(9)
# s.remove(9)
# print(0 in s)
# print(s)
# print(len(s))
