#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (48.47%)
# Likes:    3009
# Dislikes: 432
# Total Accepted:    769.3K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = dummy_node = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                l1 = l1.next

            head = head.next

        if l1:
            head.next = l1

        if l2:
            head.next = l2

        # if l1 0r l2:
        #   head.next = l1 or l2

        return dummy_node.next
# @lc code=end
