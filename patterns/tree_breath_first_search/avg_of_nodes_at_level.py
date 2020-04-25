"""
Given a binary tree, populate an array to represent the
averages of all of its levels.
"""

# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_nodes = len(queue)
        sum_ = 0
        for i in range(level_nodes):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            sum_ += node.val

        result.append(sum_ / level_nodes)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
