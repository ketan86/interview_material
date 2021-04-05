"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""
# pylint: skip-file

import heapq


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    # min_heap to maintain the min elements
    min_heap = []
    # new linked list head
    new_ll_head = None
    # insert root elements of each list to min heap.
    for ll in lists:
        heapq.heappush(min_heap, ll)

    # pop min node and keep adding next node to the heap.
    while min_heap:
        # pop item from the min heap
        ll = heapq.heappop(min_heap)
        # form, new link list if it's none, else set next of the new ll to
        # current node and move new ll to next node
        if new_ll_head is None:
            new_ll_head = ll
        else:
            new_ll_head.next = ll
            new_ll_head = new_ll_head.next

        # if next node is not none, add it to min_heap
        if ll.next is not None:
            heapq.heappush(min_heap, ll.next)

    return new_ll_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='\n')
        result = result.next


main()
