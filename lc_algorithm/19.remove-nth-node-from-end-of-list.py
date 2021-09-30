#
# @lc app=leetcode id=19 lang=python3
# Medium
# [19] Remove Nth Node From End of List
#

# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

# Follow up: Could you do this in one pass?


# Example 1:


# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1, 2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Runtime: 28 ms, faster than 92.05%"""
        if not head:
            return head

        slow = head
        fast = head

        # move fast pointers n-1 forward
        fast = self.move_forward(fast, n-1)

        # move fast pointer till end
        prev = None
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        # remove the node at slow pointer
        if prev:
            prev.next = slow.next
        else:
            head = slow.next

        return head

    def move_forward(self, node, n):
        while n:
            node = node.next
            n -= 1
        return node

# @lc code=end
