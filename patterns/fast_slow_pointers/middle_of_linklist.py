# pylint: skip-file
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def find_middle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
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
