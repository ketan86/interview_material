#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.61%)
# Likes:    5771
# Dislikes: 1484
# Total Accepted:    978.2K
# Total Submissions: 3.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = 0
        n2 = 0
        l1_head = l1
        l2_head = l2

        while l1:
            n1 += 1
            l1 = l1.next
        while l2:
            n2 += 1
            l2 = l2.next

        l1 = l1_head
        l2 = l2_head

        if n2 > n1:
            l1 = l2_head
            l2 = l1_head
            l1_head = l1
            l2_head = l2

        carry = 0
        prev_l1 = l1
        while l1:
            if l2:
                sum_ = l1.val + l2.val + carry
            else:
                sum_ = l1.val + carry
            carry = sum_ // 10
            if sum_ > 9:
                l1.val = sum_ % 10
            else:
                l1.val = sum_
            prev_l1 = l1
            if l2:
                l2 = l2.next
            l1 = l1.next

        if carry > 0:
            prev_l1.next = ListNode(carry)

        return l1_head

    def addTwoNumbers1(self, l1, l2):
        n1 = 0
        n2 = 0
        l1_head = l1
        l2_head = l2

        while l1:
            n1 += 1
            l1 = l1.next
        while l2:
            n2 += 1
            l2 = l2.next

        l1 = l1_head
        l2 = l2_head

        if n2 > n1:
            l1 = l2_head
            l2 = l1_head
            l1_head = l1
            l2_head = l2

        carry = 0
        prev_l1 = l1
        while l1:
            if l2:
                carry, sum_ = divmod(l1.val + l2.val + carry, 10)
            else:
                carry, sum_ = divmod(l1.val + carry, 10)
            l1.val = sum_
            prev_l1 = l1
            if l2:
                l2 = l2.next
            l1 = l1.next

        if carry > 0:
            prev_l1.next = ListNode(carry)

        return l1_head
# @lc code=end
