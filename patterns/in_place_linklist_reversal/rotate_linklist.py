"""
Given the head of a LinkedList and a number ‘k’, reverse every alternating
‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements,
reverse it too.


for ex, k = 3

from = head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
to   = head -> 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> null


for ex, k = 8

from = head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
to   = head -> 3 -> 4 -> 5 -> 1 -> 2 -> null

"""
# pylint: skip-file


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, k):
    start = head
    index = 0
    # loop over the link list multiple times if required until the index
    # matches the rotation count.
    while index != k:
        curr = start
        while curr:
            curr = curr.next
            index += 1
            if index == k:
                break

    # one we find the node where first node should be places,
    # move both start and end pointers and till you reach the end.
    while curr.next:
        start = start.next
        curr = curr.next

    temp = start.next
    start.next = curr.next
    curr.next = head
    head = temp

    return head


# second solution to find the length and calculate the index position
# using the math.
# nodes_to_skip = k % length
# skip set of nodes and then move pointers.
def rotate(head, k):
    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    # connect the last node with the head to make it a circular list
    last_node.next = head

    # no need to do rotations more than the length of the list
    k %= list_length
    skip_length = list_length - k
    last_node_of_rotated_list = head

    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    # 'last_node_of_rotated_list.next' is pointing to the
    # sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
