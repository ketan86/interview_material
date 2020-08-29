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


"""
NOTE: Key here is to make sure both lists are merged correctly and it depends
on the nodes count. make sure right linkedlist is smaller then left or
wiseversa.
    # odd elements -> slow is set to mid (1 2 3 4 5 6 7) -> 4
        - left -> 1 2 3 4 , right -> 5 6 7
        - 1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4
        when merged, use right node to stop merging when right node is none.
        remaining node (4) in left will get attached to 7 when loop
        breaks.
    # even elements -> slow is set to mid + 1 (1 2 3 4) -> 3
        - left -> 1 2 3 , right -> 4
        - 1 -> 4 -> 2 -> 3
        when merged, use right node to stop merging when right node is none.
        node 4 next attaches to 2 when loop breaks and 2 is already attached
        to node 3.
"""


def rearrange(head):
    # find the middle node.
    mid = find_mid(head)
    # reverse the linklist from mid.next node
    right = reverse(mid.next)
    # detach the left and right node by setting the mid.next to None.
    mid.next = None
    # merge left(head) and right linked list.
    head = merge(head, right)

    _print(head)


def find_mid(head):
    # find middle of the linked list using slow and fast pointer approach.
    # odd elements -> slow is set to mid (1 2 3 4 5 6 7) -> 4
    # even elements -> slow is set to mid + 1 (1 2 3 4) -> 3
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(head):
    # reverse the linked list
    curr = head
    nxt = curr.next
    curr.next = None
    while nxt:
        temp = nxt.next
        nxt.next = curr
        curr = nxt
        nxt = temp
    return curr


def merge(left, right):
    # save head
    head = left
    # use right linkedlist (smaller than left) to merge.
    while right:
        next_left = left.next
        next_right = right.next
        left.next = right
        right.next = next_left
        left = next_left
        right = next_right
    # when right linkedlist is iterated, nodes left in the left linkedlist
    # is already in order.
    return head


def rearrange_2(head):
    # find the middle and divide in half, reverse the second half and
    # swap data.
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow = _reverse_2(slow)
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


def _reverse_2(node):
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
    print("LinkedList rearrange: " + str(rearrange(head)))
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
