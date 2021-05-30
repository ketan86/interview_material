from singly_linked_list import SinglyLinkedList


def remove_duplicates(lst):
    # copy the head
    curr = lst.head
    # if head is none, return
    if curr is None:
        return lst
    # copy the node values into set
    visited = set()
    # save prev pointer
    prev = None
    # loop over till end
    while curr:
        # if we find the node that is visited,
        # delete that. else, add to set
        if curr.data in visited:
            prev.next = curr.next
        else:
            visited.add(curr.data)
        # move prev and curr pointer
        prev = curr
        curr = curr.next

    return lst


s = SinglyLinkedList()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
s.add(1)
print(s)
print(remove_duplicates(s))
