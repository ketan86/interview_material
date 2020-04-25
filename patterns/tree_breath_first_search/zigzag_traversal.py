"""
Given a binary tree, populate an array to represent its zigzag level order
traversal. You should populate the values of all nodes of the first level
from left to right, then right to left for the next level and keep
alternating in the same manner for the following levels.

         1
        / \
       2   3
      / \ / \
     4  5 6  7

[[1],[3,2],[4,5,6,7]]

"""

# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    level = 0
    while queue:
        level_length = len(queue)
        # this is the key, lets you append nodes from left to right and
        # right to left efficiently.
        level_results = deque()
        for i in range(level_length):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if level % 2 == 1:
                level_results.appendleft(node.val)
            else:
                level_results.append(node.val)
        result.append(list(level_results))
        level += 1
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
