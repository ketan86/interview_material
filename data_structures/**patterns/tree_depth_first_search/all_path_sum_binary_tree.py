"""
This pattern is based on the Depth First Search (DFS) technique to
traverse a tree.

We will be using recursion (or we can also use a stack for the
iterative approach) to keep track of all the previous (parent)
nodes while traversing. This also means that the space complexity
of the algorithm will be O(H), where ‘H’ is the maximum height of
the tree.

Let’s jump onto our first problem to understand this pattern.
"""
# pylint: skip-file


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum_):
    # store results
    all_paths = []
    # traverse the tree from root and
    _traverse(root, sum_, all_paths)
    # return the results
    return all_paths


def _traverse(root, sum_, paths, path=None):
    # **NOTE*: Never set path=[] empty list in the args. It will yield unexpected results

    # if path is None, set to empty list
    if path is None:
        path = []

    # if root node is none, return
    if root is None:
        return

    # add root node to path
    path.append(root.val)

    # if root sum is same as given sum and leaf node, capture the path
    # for left and right traversal, reduce the sum value by removing the
    # root element value at every step.
    if sum_ == root.val and root.left is None and root.right is None:
        # this is the key, if new list is not created, values from the path
        # is removed eventually and so from the paths list.
        paths.append(list(path))

    # traverse left and right
    _traverse(root.left, sum_ - root.val, paths, path)
    _traverse(root.right, sum_ - root.val, paths, path)

    # remove the root when both left and right returns.
    path.pop()


"""
OUTPUT:

[12]
[12, 7]
[12, 7, 4]
appended
[12, 1]
[12, 1, 10]
appended
[12, 1, 5]
Tree paths with sum 23: [[12, 7, 4], [12, 1, 10]]
"""


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum_ = 23
    print("Tree paths with sum " + str(sum_) +
          ": " + str(find_paths(root, sum_)))


main()
