# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.mark = False


# solution 1 - slow pointer marks the node it visits, when fast pointer
# discovers the first marked node, we find the start of the circle.
def find_cycle_start(head):
    # copy head to slow and fast
    slow, fast = head, head
    # until fast pointer and fast.next pointer is not None
    while fast and fast.next:
        # if fast pointer find the marker, return node
        if fast.mark:
            return fast.data
        # fast moves two steps
        fast = fast.next.next
        # slo create a marker
        slow.mark = True
        # slo moves one step
        slow = slow.next


def find_cycle_start(head):
    """
    1. find circle length (when slo and fast pointers meet)
    2. move fast pointer to circle length
    3. move slow and fast pointer one step at a time until they meet.
    """
    # find the length of the circle
    length = find_cycle_length(head)

    if length > 0:
        # fast and slow pointer
        fast, slow = head, head
        # move fast pointer circle length
        while length > 0:
            fast = fast.next
            length -= 1

        # until slow pointer meets fast, move both slow and fast pointers one
        # step at a time.
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.data


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
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head)))


main()
