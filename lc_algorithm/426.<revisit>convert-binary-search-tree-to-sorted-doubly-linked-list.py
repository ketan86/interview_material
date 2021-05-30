#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (57.95%)
# Likes:    840
# Dislikes: 88
# Total Accepted:    69.2K
# Total Submissions: 119.3K
# Testcase Example:  '[4,2,5,1,3]'
#
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
# place.
#
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation, the left
# pointer of the tree node should point to its predecessor, and the right
# pointer should point to its successor. You should return the pointer to the
# smallest element of the linked list.
#
#
# Example 1:
#
#
#
#
# Input: root = [4,2,5,1,3]
#
#
# Output: [1,2,3,4,5]
#
# Explanation: The figure below shows the transformed BST. The solid line
# indicates the successor relationship, while the dashed line means the
# predecessor relationship.
#
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [1,2,3]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
#
#
# Example 4:
#
#
# Input: root = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# All values of Node.val are unique.
# 0 <= Number of Nodes <= 2000
#
#
#

# @lc code=start
# pylint:skip-file

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionGen:
    """
    This solution violates the requirement of converting the
    existing tree to sorted linked list but gives an interesting
    usecase of generator.
    """

    def treeToDoublyListGenerator(self, root):
        if not root:
            return root

        # define a generator to traverse tree in-order
        def gen_inorder(node):
            if node:
                yield from gen_inorder(node.left)
                yield node
                yield from gen_inorder(node.right)

        # set head and tail to None
        head = None
        tail = head

        for node in gen_inorder(root):
            # if tail node is not None, set tail's right to
            # current node and node's left to tail
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node

            # move the tail to current node
            tail = node

        # create cycle
        head.left = tail
        tail.right = head

        # return start
        return head


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def helper(root):
            if root is None:
                return None, None

            left_head, left_tail = helper(root.left)
            # the tail of left tree and the root should be connected
            if left_tail:
                left_tail.right = root
                root.left = left_tail
            else:
                # leaf node case, we need to specify leftHead is the leaf itself
                left_head = root

            right_head, right_tail = helper(root.right)
            # the head of right tree and the root should be connected
            if right_head:
                right_head.left = root
                root.right = right_head
            else:
                # leaf node case, we need to specify rightTail is the leaf itself
                right_tail = root
            # return the left most node and the right most node at this node
            return left_head, right_tail

        if root is None:
            return root

        head, tail = helper(root)
        # connect head and tail together
        head.left = tail
        tail.right = head

        return head


class Solution:
    head = None
    tail = None

    def treeToDoublyList(self, root):
        """
        The problem statement here is to convert the existing
        binary search tree to sorted doubly linked list instead
        of forming the new linked list.

        For ex,
                             4
                         /       \
                        2         6
                      /   \     /
                    1       3  5

            1 -> 2 -> 3 -> 4 -> 5 -> 6 ->1 (circular)

        so at every root, the root's left is a tail and tail's
        right is a root. for ex, at root 4, 4's left is a last
        visited root, and last visited root, 3's right is 4.

        if there is no tail, current node is the head. we only
        have to set the head once when root is 1. at that time,
        tail is also root.

        we can store head and tail globally.
        """
        # IMP:-> The idea here is to set the head node when tail is none,
        # else use tail node to attach a new root node and move the
        # tail to new node.
        def dfs(node):
            if not node:
                return

            # left traversal
            dfs(node.left)

            # if tail is None, set the head for the first time
            if not self.tail:
                self.head = node
            else:
                # else, current node's left is tail and tail's
                # right is current node
                node.left = self.tail
                self.tail.right = node

            # move tail to next node
            self.tail = node

            # right traversal
            dfs(node.right)

        dfs(root)

        # if we have the head set, create a circular link
        if self.head:
            self.head.left = self.tail
            self.tail.right = self.head

        # return the head
        return self.head

# t = Node(2)
# t.left = Node(1)
# t.right = Node(3)
# s = SolutionGen()
# head = s.treeToDoublyListGenerator(t)
# import pdb;pdb.set_trace()
# @lc code=end
