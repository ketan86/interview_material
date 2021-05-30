"""
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’
sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, 
reverse it too.

for ex, k = 2

from = head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
to = head -> 2 -> 1 -> 4 -> 3 -> 5 -> null

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


def reverse_every_k_elements(head, k):
    curr = head
    prev = None
    while curr:
        start, end, next_ = _reverse(curr, k)
        if prev is None:
            head = end
        else:
            prev.next = end
        prev = start
        curr = next_
    return head


def _reverse(head, k):
    total = 0
    start = end = head
    prev = None
    while end:
        nxt = end.next
        end.next = prev
        prev = end
        end = nxt
        total += 1
        if total == k:
            break
    start.next = end
    return start, prev, end


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
