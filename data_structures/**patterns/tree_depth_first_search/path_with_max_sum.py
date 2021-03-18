"""
Given a binary tree, find the root-to-leaf path with the maximum sum.
"""
"""
Given a binary tree, return all root-to-leaf paths.
"""
# pylint: skip-file


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root):
    return _traverse(root, 0)


def _traverse(root, max_sum, path=None):
    # **NOTE*: Never set path=[] empty list in the args. It will yield unexpected results

    # if path is None, set to empty list
    if path is None:
        path = []

    # if root is None, return the max_sum
    if root is None:
        return max_sum

    # append root in the path
    path.append(root.val)

    # if leaf node
    if not root.left and not root.right:
        # find max sum so far against the path sum
        max_sum = max(max_sum, sum(list(path)))

    # capture the max_sum
    max_sum = _traverse(root.left, max_sum, path)
    max_sum = _traverse(root.right, max_sum, path)

    # pop the root node
    path.pop()

    # return the max sum
    return max_sum


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(35)
    print("Tree path with max sum: " + str(find_paths(root)))


main()
