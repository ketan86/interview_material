# Given the root of a binary tree, collect a tree's nodes as if
# you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.

# Example 1:


# Input: root = [1, 2, 3, 4, 5]
# Output: [[4, 5, 3], [2], [1]]
# Explanation:
# [[3, 5, 4], [2], [1]] and [[3, 4, 5], [2], [1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
# Example 2:

# Input: root = [1]
# Output: [[1]]


# Constraints:

# The number of nodes in the tree is in the range[1, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root):
        """
        Runtime: 32 ms, faster than 57.48%


        In binary tree the height of the node is 1 + max(left, right). Using
        above formula we can find the depth of the node where result has to
        be placed.

                     1 h=2
                   /   \
     h=1          2     3 h=0
                /  \
     h=0       4    5

        for ex, dfs with post-order-traversal (in order to find the root node
        height, we need both left and right heights first),
            at node 4 -> height(left) = -1 , height(right) = -1 => 1 + max(-1, -1) = 0
                         result[0] = [4]
               node 1 -> height(left) = 2 , height(right) = 1 => 1 + 2 = 3
                         result[2] = [1]

        """
        result = []

        def find_height(node):
            if not node:
                return -1

            # find height of both left and right child first
            left_height = find_height(node.left)
            right_height = find_height(node.right)

            # find current height
            curr_height = 1 + max(left_height, right_height)

            # if curr height == len(result), we need to create a new list
            if len(result) == curr_height:
                result.append([])

            # append node at height index
            result[curr_height].append(node.val)

            # return current height
            return curr_height

        find_height(root)

        return result
