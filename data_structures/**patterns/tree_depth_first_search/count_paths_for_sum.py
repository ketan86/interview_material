"""
Given a binary tree and a number ‘S’, find all paths in the tree such
that the sum of all the node values of each path equals ‘S’. Please
note that the paths can start or end at any node but all paths must
follow direction from parent to child (top to bottom).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, sum_):
    return _traverse(root, sum_)


def _traverse(root, sum_, path=None):
    # **NOTE*: Never set path=[] empty list in the args. It will yield unexpected results

    # if path is None, set to empty list
    if path is None:
        path = []

    # if root is none, count is 0
    if root is None:
        return 0

    # add root to the path
    path.append(root.val)

    # sum_path values and if it's == sum, capture the count
    path_sum = count = 0
    for i in reversed(path):
        path_sum += i
        if path_sum == sum_:
            count += 1

    # traverse left and right and add count to it
    count += _traverse(root.left, sum_, path)
    count += _traverse(root.right, sum_, path)

    # remove the current node to backtrack
    path.pop()

    # return the count
    return count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Tree has paths: " + str(count_paths(root, 12)))


main()
