"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList
such that the nodes from the second half of the LinkedList are inserted
alternately to the nodes from the first half in reverse order. So if the
LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should
return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
"""
# pylint: skip-file


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def rearrange(head):
    # find the middle and divide in half, reverse the second half and
    # swap data.
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow = _reverse(slow)
    fast = head

    # 1->2->3->4->5->6
    # 1->2->3->6->5->4
    # save 2 and 5, point 1 to 6, 6 to 2, move slow and fast to 2 and 5
    while slow:
        slow_nxt = slow.next
        fast_nxt = fast.next
        fast.next = slow
        slow.next = fast_nxt
        fast = fast_nxt
        slow = slow_nxt

    # fast here is pointing to head so when slow pointer is done iterating,
    # any elements after fast should be set to None to detach the right
    # side of the list which we have reversed and stored in slow.
    if fast:
        fast.next = None

    _print(head)
    return True


def _print(node):
    while node:
        print(str(node.data) + '->')
        node = node.next


def _reverse(node):
    prev = None
    while node:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
    return prev


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # print("LinkedList rearrange: " + str(rearrange(head)))
    head.next.next.next.next.next = Node(6)
    # print("LinkedList rearrange: " + str(rearrange(head)))
    head.next.next.next.next.next.next = Node(7)
    print("LinkedList rearrange: " + str(rearrange(head)))
    # head.next.next.next.next.next.next.next = Node(8)
    # print("LinkedList rearrange: " + str(rearrange(head)))
    # head.next.next.next.next.next.next.next.next = Node(9)
    # print("LinkedList rearrange: " + str(rearrange(head)))


main()
