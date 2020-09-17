# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_cycle_length(head):
    # define slow and fast pointers
    slow, fast = head, head
    # if fast and fast.next is not None.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # when both pointers meet, it's a start of the cycle.
        if slow == fast:
            return _find_length(slow)
    return 0


def _find_length(slow):
    # copy the slow pointer location and move the pointer until the slow
    # pointer again meets the copied slow pointer. keep counting the node
    # along the way.
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
