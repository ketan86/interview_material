from singly_linked_list import SinglyLinkedList


def find_mid(ll):
    # copy head pointer
    node = ll.head
    # if head is None, return
    if not node:
        return
    # use slow and fast pointer approach to
    # find the middle node. By moving slow
    # pointer by 1 step and fast by 2 step,
    # slow pointer will be in the middle when
    # fast pointer reaches end or crosses end.
    slow = node
    fast = node

    # loop over using fast pointer
    while fast:
        # move fast pointer one step forward
        fast = fast.next
        # if fast pointer is not at the end, move
        # one more step forward.
        if fast:
            # move slow pointer one step forward
            slow = slow.next
            fast = fast.next
    # when exit, slow pointer would in the middle node.
    return slow.data


s = SinglyLinkedList()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(find_mid(s))
