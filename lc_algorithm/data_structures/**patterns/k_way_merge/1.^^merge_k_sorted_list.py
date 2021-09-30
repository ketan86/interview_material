"""
You are given an array of k linked-lists lists, each linked-list is sorted 
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
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
