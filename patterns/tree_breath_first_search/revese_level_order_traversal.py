"""
Given a binary tree, populate an array to represent its level-by-level
traversal in reverse order, i.e., the lowest level comes first.
You should populate the values of all nodes in each level from
left to right in separate sub-arrays.

         1
        / \
       2   3
      / \ / \
     4  5 6  7

[[4,5,6,7],[2,3],[1]]
"""
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_nodes = []
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_nodes.append(node.val)
        result.appendleft(level_nodes)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
