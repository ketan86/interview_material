# Given the root of a binary search tree, a target value, and an integer k,
# return the k values in the BST that are closest to the target. You may return
# the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are
# closest to the target.

# Example 1:


# Input: root = [4, 2, 5, 1, 3], target = 3.714286, k = 2
# Output: [4, 3]
# Example 2:

# Input: root = [1], target = 0.000000, k = 1
# Output: [1]


# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104.
# 0 <= Node.val <= 109
# -109 <= target <= 109

# Follow up: Assume that the BST is balanced. Could you solve it in less than
# O(n) runtime(where n=total nodes)?


# Definition for a binary tree node.
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def closestKValuesHeap(self, root: TreeNode, target: float, k: int):
        """
        Time  -> O(n log k)
        Space -> O(k + H) to keep the heap of the k elements and recursion
                 stack of the tree height
        Runtime: 44 ms, faster than 87.61% """

        # max heap to store top k closest difference
        closest_values = []

        self.dfs(root, target, k, closest_values)

        return [node for d, node in closest_values]

    def dfs(self, node, target, k, closest_values):
        if not node:
            return

        # left traversal
        self.dfs(node.left, target, k, closest_values)

        diff = abs(node.val - target)

        # until we have enough elements
        if len(closest_values) < k:
            heapq.heappush(closest_values, (-diff, node.val))
        else:
            # else, replace the top element if diff is less than the top element
            if closest_values and diff < -closest_values[0][0]:
                heapq.heapreplace(closest_values, (-diff, node.val))

        # right traversal
        self.dfs(node.right, target, k, closest_values)

    # def closestKValuesSort(self, root: TreeNode, target: float, k: int):
    #     """
    #     Time -> O(n log n). O(n) for traversal and O(n log n) for sort
    #     Space -> O(n)

    #     Runtime: 48 ms, faster than 74.12%"""
    #     def inorder(r: TreeNode):
    #         return inorder(r.left) + [r.val] + inorder(r.right) if r else []

    #     nums = inorder(root)
    #     nums.sort(key=lambda x: abs(x - target))
    #     return nums[:k]
