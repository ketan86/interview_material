#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (34.12%)
# Likes:    3721
# Dislikes: 708
# Total Accepted:    445.5K
# Total Submissions: 1.2M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
#
#
#
# Constraints:
#
#
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
#
#
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        "Runtime: 36 ms, faster than 62.90%"
        # if not head, return
        if not head:
            return head

        # use dict to store the given node and the pointer to new node
        d = {}
        # copy head so we can loop again
        node = head
        # create a first result node
        result = Node(node.val)
        # store a reference from give node to newly created node. if someone
        # is pointing to node 7 of original list, a new node would be stored
        # to create a random pointer.
        d[node] = result
        # copy result head node
        result_head = result

        # start from second node. result stays one node behind so we can point
        # next new node to node.
        while node.next:
            # create a new node and assign result's next to new node
            new_node = Node(node.next.val)
            result.next = new_node
            # create node and new node reference
            d[node.next] = new_node
            # move both nodes
            node = node.next
            result = result.next

        # copy head and result head
        node = head
        new_node = result_head
        # both head should be at the same node level
        while node:
            # create a random pointer and move both nodes
            new_node.random = d.get(node.random, None)
            new_node = new_node.next
            node = node.next

        return result_head

# @lc code=end
