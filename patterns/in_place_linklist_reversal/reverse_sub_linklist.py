"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’,
reverse the LinkedList from position ‘p’ to ‘q’.

from = head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
to = head -> 1 -> 4 -> 3 -> 2 -> 5 -> null
"""

# pylint: skip-file


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    curr = head
    prev = None
    # set curr to head and prev to None.
    # for every iteration, prev is one step behind curr.
    while curr:
        # when curr value matches the reversal node start
        if curr.value == p:
            # send current node pointer and end node value to reverse the
            # sublist.
            start = _reverse_sublist(curr, q)
            # if prev node is None, return start, start is the start of the ll
            # else, point prev node next to start.
            if prev is not None:
                prev.next = start
                return head
            else:
                return start
        # keep moving until the first node is found, If not found, ll is
        # unchanged.
        prev = curr
        curr = curr.next
    return prev


def _reverse_sublist(head, q):
    # save head to start
    start = head
    # set end and next_ (a pointer next to the end node) to None.
    end = None
    next_ = None
    # reverse algorithm
    while start:
        nxt = start.next
        start.next = end
        end = start
        # when we reach the last node, save the next pointer.
        # it could be None or more nodes.
        # break after end node is reversed.
        if start.value == q:
            next_ = nxt
            break
        start = nxt
    # set head next pointer to next_
    #  for ex, 1 2 3 4 5 6 7 8 9
    #            ^         ^
    #            head      end
    # head points to 8 now.
    head.next = next_
    # return the end, which is the start of the sublist now.
    return end


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 1, 7)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
