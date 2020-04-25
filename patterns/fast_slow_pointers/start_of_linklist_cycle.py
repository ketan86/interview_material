# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.mark = False


# solution 1 - slow pointer marks the node it visits, when fast pointer
# discovers the first marked node, we find the start of the circle.
def find_cycle_start(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        if fast.mark:
            return fast.data
        fast = fast.next.next
        slow.mark = True
        slow = slow.next

# solution 2 - fast pointers moves circle length times compare to slow pointer
# that moves 1 step.
# or   =========
# fast pointer moves only once the circle length and then both moves one step
# until they meet.


def find_cycle_start(head):
    length = find_cycle_length(head)
    print(length)
    if length > 0:
        fast, slow = head, head
        while length > 0:
            fast = fast.next
            length -= 1

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow.data


def _move_pointer(pointer, times):
    for i in range(times):
        pointer = pointer.next
    return pointer


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
    count = 1
    while curr.next != slow:
        curr = curr.next
        count += 1
    return count


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head)))


main()
