"""
Given a binary tree, populate an array to represent its level-by-level
traversal. You should populate the values of all nodes of each level
from left to right in separate sub-arrays.

         1
        / \
       2   3
      / \ / \
     4  5 6  7

[[1],[2,3],[4,5,6,7]]

"""

# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    if root:
        queue.append(root)
        queue.append(None)

    level_results = []
    while len(queue) > 0:
        node = queue.popleft()
        if node is not None:
            level_results.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            result.append(level_results)
            level_results = []
            queue.append(None)
            if len(queue) == 1:
                break

    return result


# second approach
def traversal(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            # insert the children of current node in the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
