"""
This pattern is based on the Depth First Search (DFS) technique to
traverse a tree.

We will be using recursion (or we can also use a stack for the
iterative approach) to keep track of all the previous (parent)
nodes while traversing. This also means that the space complexity
of the algorithm will be O(H)O(H), where ‘H’ is the maximum height of the tree.

Let’s jump onto our first problem to understand this pattern.
"""
# pylint: skip-file


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, exp_sum, curr_sum=0):
    # if root is None, return False
    if root is None:
        return False

    # add root value to curr sum
    curr_sum += root.val
    # sum is found and leaf node.
    if curr_sum == exp_sum and root.left is None and root.right is None:
        return True

    # go left and right
    # if either left or right is true, we found the path.
    left = has_path(root.left, exp_sum, curr_sum)
    if left:
        return True

    right = has_path(root.right, exp_sum, curr_sum)
    if right:
        return True

    return False

# Short version


def has_path_short_version(root, sum_):
    if not root:
        return False

    # if the current node is a leaf and its value is equal to the sum,
    # we've found a path
    if root.val == sum_ and not root.left and not root.right:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, sum_ - root.val) \
        or has_path(root.right, sum_ - root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))
    print("Tree has path: " + str(has_path_short_version(root, 23)))
    print("Tree has path: " + str(has_path_short_version(root, 16)))


main()
