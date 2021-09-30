#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (39.03%)
# Likes:    5184
# Dislikes: 300
# Total Accepted:    686.8K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Given an array of linked-lists lists, each linked list is sorted in ascending
# order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
# Example 1:
#
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
#
# Example 2:
#
#
# Input: lists = []
# Output: []
#
#
# Example 3:
#
#
# Input: lists = [[]]
# Output: []
#
#
#
# Constraints:
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    N => n nodes of k linked list (n*k)

    Naive approach: Collect all nodes values and store it in a list and then
    using sort function, sort values and recreate a new linkedlist.
    T -> O(N log N)
    S -> O(N)

    Priority Queue:
    Time Complexity    => O(N log k)
    Space Complexity => O(k)
        ```
        from Queue import PriorityQueue
        class Solution(object):
            def mergeKLists(self, lists):
                head = point = ListNode(0)
                q = PriorityQueue()
                for l in lists:
                    if l:
                        q.put(l)
                while not q.empty():
                    node = q.get()
                    point.next = ListNode(node.val)
                    if node.next:
                        q.put(node.next)
                    point = point.next
                return head.next
        ```
    Better Approach: Merge two sorted linked list in O(N) where n is total number
    of nodes in both list. So partition the K linked lists and merge them.
    Time Complexity => O(n * k log k) where k is the number of linked lists.
                       merge k list of n nodes with log k partition

                    => O(N log k)

    Space Complexity => O(1)
    """

    def mergeKLists(self, lists):
        """Runtime: 172 ms, faster than 25.14%"""
        # using merge sort Time => 0(N log K)
        if not lists:
            return
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, start, end):  # O(n)
        if start < end:
            mid = start + (end - start) // 2
            n1 = self.partition(lists, start, mid)
            n2 = self.partition(lists, mid + 1, end)
            return self.merge(n1, n2)
        # we only have one list so can not partition,
        # return start or end since they both are
        # same.
        return lists[start]

    def merge(self, l1, l2):  # O(k)
        head = dummy = ListNode()  # Result so not considered in space
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next

        if l1 or l2:
            head.next = l1 or l2

        return dummy.next

# @lc code=end
