"""
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree
is seen from the right side.

        12
        / \
       2   3
      / \ / \
     4  9 6  7
    /
   5

right view: 12, 3, 7, 5
"""
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    """Only include the node that is last in each level"""
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_nodes = len(queue)
        for i in range(level_nodes):
            node = queue.popleft()
            if i == level_nodes - 1:
                result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
