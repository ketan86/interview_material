# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_middle(head):
    """
    Use two pointers, slow(1 step) and fast(2 step) pointers and when fast
    pointer reaches end, slow pointer would be in the middle.
    """
    # define a slow and fast pointer
    slow, fast = head, head
    # check the fast pointer and fast's next pointer is not None.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # when fast pointer reaches the end of the linklist. slow pointer is at the
    # middle of the linklist.
    return slow.data


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("LinkedList middle: " + str(find_middle(head)))
    head.next.next.next.next.next = Node(6)
    print("LinkedList middle: " + str(find_middle(head)))
    head.next.next.next.next.next.next = Node(7)
    print("LinkedList middle: " + str(find_middle(head)))
    head.next.next.next.next.next.next.next = Node(8)
    print("LinkedList middle: " + str(find_middle(head)))


main()
