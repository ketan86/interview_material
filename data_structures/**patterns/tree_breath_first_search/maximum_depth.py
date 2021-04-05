"""
Find the maximum depth of a binary tree. The maximum depth is the number
of nodes along the shortest path from the root node to the nearest leaf node.
"""
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_maximum_depth(root):
    """ Calculate the level in DFS"""
    if root is None:
        return - 1
    level = 0
    queue = deque()
    queue.append(root)
    while queue:
        level_nodes = len(queue)
        for i in range(level_nodes):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()
