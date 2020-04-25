# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return _find_length(slow)
    return 0


def _find_length(slow):
    curr = slow
    length = 1
    while curr.next != slow:
        length += 1
        curr = curr.next
    return length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
