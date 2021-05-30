# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_cycle(head):
    # defind a slow and fast pointer
    slow, fast = head, head

    # if fast and fast.next pointers are not None.
    while fast and fast.next:
        # take two steps
        fast = fast.next.next
        # take one step
        slow = slow.next
        # when slow and fast pointers meet, cycle is found. else continue.
        if slow == fast:
            return True

    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    print("LinkedList cycle: " + str(find_cycle(head)))
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle: " + str(find_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle: " + str(find_cycle(head)))


main()
