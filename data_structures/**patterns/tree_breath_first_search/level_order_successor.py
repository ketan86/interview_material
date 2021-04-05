"""
Given a binary tree and a node, find the level order successor of the
given node in the tree. The level order successor is the node that
appears right after the given node in the level order traversal.


         12
        / \
       2   3
      / \ / \
     4  9 6  7

node : 2 -> level order successor 3
node : 12 -> level order successor 2
node : 3 -> level order successor 4
"""
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    # if root is None, return
    if root is None:
        return
    # define queue and add root to it
    queue = deque()
    queue.append(root)
    # use a flag to mark the node when found
    found = False
    while queue:
        node = queue.popleft()
        # if node was found, current node is the successor
        if found:
            return node
        # if node is found, set found to True
        if node.val == key:
            found = True
        # left and right traversal
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
