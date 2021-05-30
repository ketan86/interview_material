# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_cycle_length(head):
    """
    Using slow and fast pointers, it is not gurrantied that slow and fast
    pointers will meet at the start of the cycle. It can meet anywhere in
    the cycle. Once we find the meeting point, we have to run another pointer
    from meeting point till it comes back to same point to find the length
    of the circle.
    """
    # keep moving slo and fast pointer until they meet.
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # when slo and fast pointers meet, we are in the circle somewhere so
        # find the length of the circle by keeping one pointer there and running
        # another pointer on the circle until both pointers meet.
        if slow == fast:
            # once slow and fast pointers meet, we have to find the length
            # of the circle.
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
    head.next.next.next.next.next.next = head.next.next.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
