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
        """Runtime: 72 ms, faster than 47.84%"""
        # init dummy node with 0 value
        dummy_node = ListNode(0)

        # copy pointers
        p = l1
        q = l2
        curr = dummy_node

        # init carry with 0
        carry = 0

        # until either p or q linked list is empty
        while p or q:
            # if either one is empty, set it's value to 0
            x = 0 if not p else p.val
            y = 0 if not q else q.val

            # find sum and carry
            sum_ = carry + x + y
            carry = sum_ // 10

            # create a new node with 1 digit
            curr.next = ListNode(sum_ % 10)
            curr = curr.next

            # if p and q are not None, go to next node
            if p:
                p = p.next
            if q:
                q = q.next

        # if carry is left at the end, create a new node
        if carry > 0:
            curr.next = ListNode(carry)

        # return linked list starting from second node.
        return dummy_node.next

    def addTwoNumbersNotSoElegant(self, l1, l2):
        n1 = 0
        n2 = 0
        l1_head = l1
        l2_head = l2

        #######
        # This can be avoided by using 0 when node is null.
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
        #######
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

# @lc code=end
