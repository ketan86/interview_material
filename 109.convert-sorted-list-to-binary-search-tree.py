#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (42.04%)
# Likes:    1698
# Dislikes: 85
# Total Accepted:    228K
# Total Submissions: 497.3K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        This algorithm follows the same pattern as 108.convert-sorted-array-
        to-binary-search-tree.py except we have to work with linked list.
        """
        def create_bst(head):
            # if linked list head is none, return None.
            if head is None:
                return

            # find the middle and prev node of the linked list
            mid_ll_node, prev_node = self._find_mid(head)

            # create a root node with the middle element value.
            root = TreeNode(mid_ll_node.val)

            # store all nodes from mid + 1 to a head that is used for
            # right side search for right tree node.
            right_head = mid_ll_node.next

            # detach all nodes from prev node to end node. this new
            # linked list will be used to search the left element.
            left_head = head
            if prev_node is not None:
                prev_node.next = None
            else:
                # KEY:: when prev node is none, we at head. done on left side.
                left_head = None

            # iter over left and right side
            root.left = create_bst(left_head)
            root.right = create_bst(right_head)

            # return root node.
            return root

        return create_bst(head)

    def _find_mid(self, head):
        slow = fast = head
        prev = None
        while fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
            # KEY:: directly setting fast = fast.next.next will break if
            # fast is second last node. so check one step at a time.
            if fast.next is not None:
                fast = fast.next

        return slow, prev


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(10)
# head.next.next.next.next.next.next.next.next.next.next = ListNode(11)
# head.next.next.next.next.next.next.next.next.next.next.next = ListNode(12)
# head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(13)
# print(Solution().sortedListToBST(head))
# @lc code=end
