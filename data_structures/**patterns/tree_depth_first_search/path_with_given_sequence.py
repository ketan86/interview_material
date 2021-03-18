"""
Given a binary tree and a number sequence,
find if the sequence is present as a root-to-leaf path in the given tree.

Sequence: [1, 9, 9]
Output: true

Sequence: [1, 7, 2]
Output: no

    1
   / \
 7     9
 |    / \
 9  2     9
"""

# pylint: skip-file


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return _traverse(root, sequence, level=0)


def _traverse(root, sequence, level):
    if root is None:
        return False

    # if we are over the sequence level or value at the level is not same as
    # root value, stop the search and return False
    if level >= len(sequence) or sequence[level] != root.val:
        return False

    # if node is leaf node and it's a last lever, return true
    # if we reach here, we have already checked that the last node
    # has the matching value in the sequence.
    if root.left is None and root.right is None and level == len(sequence) - 1:
        return True

    # if sequence is found in left sub tree, return without searching in the
    # right subtree.
    left = _traverse(root.left, sequence, level + 1)
    if left:
        return True
    right = _traverse(root.right, sequence, level + 1)

    if right:
        return True
    return False


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
