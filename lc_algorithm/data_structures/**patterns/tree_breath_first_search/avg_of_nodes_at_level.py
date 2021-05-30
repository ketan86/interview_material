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
    # define results list to store the level avg
    result = []
    # if root is None, return result
    if root is None:
        return result
    # use queue for bfs
    queue = deque()
    # add root node to queue
    queue.append(root)
    # while queue is not empty
    # (deque implement __len__ for while loop termination )
    while queue:
        # find the total nodes at each level
        total_nodes = len(queue)
        # define the sum to 0
        sum_ = 0
        # dequeue all nodes
        for i in range(total_nodes):
            node = queue.popleft()
            # append left and right node if not None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # find the sum
            sum_ += node.val
        # save avg into the result
        result.append(sum_ / total_nodes)
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
