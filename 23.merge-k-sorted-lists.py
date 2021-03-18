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
    def mergeKLists(self, lists):
        # using merge sort Time => 0(N log K)
        if not lists:
            return
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, start, end):
        if start < end:
            mid = start + (end - start) // 2
            n1 = self.partition(lists, start, mid)
            n2 = self.partition(lists, mid + 1, end)
            return self.merge(n1, n2)
        # we only have one list so can not partition,
        # return start or end since they both are
        # same.
        return lists[start]

    def merge(self, l1, l2):
        head = dummy = ListNode()
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
