from singly_linked_list import SinglyLinkedList


def find_nth(lst, n):
    # if we know the length of the ll, we
    # can find the last nth node and reach
    # there just by moving one pointer.
    l = len(lst)

    # find the node distance from the root
    advance = l - n
    # if it's negative (ll is shorther than that),
    # return -1
    if advance < 0:
        return -1
    # copy head
    curr = lst.head

    # we don't have to check the head since value of
    # the advanced variable would decide if root is
    # none or not.
    # if curr is None:
    #     return - 1

    # move curr node till we find the last nth node.
    counter = 0
    while curr.next:
        if counter == advance:
            return curr.data
        else:
            counter += 1
        curr = curr.next

    # if we can't return -1
    return -1


# two pointer method
def find_nth2(lst, n):
    # find the head
    curr = lst.head
    # if head is none, return -1
    if curr is None:
        return -1
    # use two pointers
    first = curr
    second = curr
    # move first pointer to n steps to keep
    # two pointers n step apart, once
    # first pointer reaches the end, second
    # pointer would be at the last nth pos.
    counter = 1
    # move first pointer to n step
    while first.next:
        if counter == n:
            break
        first = first.next
        counter += 1
    # if first pointer reaches end, we can't
    # find the nth node, return -1
    else:
        return -1

    # while first reaches the end, keep
    # moving both pointers
    while first.next:
        first = first.next
        second = second.next

    # when first reches the end, second pointer
    # would be at the last nth node.
    return second.data


s = SinglyLinkedList()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(find_nth(s, 3))
