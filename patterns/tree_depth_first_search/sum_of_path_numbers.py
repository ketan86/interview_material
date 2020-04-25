"""
Given a binary tree where each node can only have a digit (0-9) value,
each root-to-leaf path will represent a number. Find the total sum of
all the numbers represented by all paths.

         1
        / \
       2   3
      / \ / \
     4  5 6  7

sum = 124 + 125 + 136 + 137 = 522
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_helper(root, val_so_far):
    if root.left is None and root.right is None:
        return int(val_so_far + str(root.val))
    else:
        left_sum = 0
        right_sum = 0
        if root.left:
            left_sum = find_sum_of_path_helper(
                root.left, val_so_far + str(root.val))
        if root.right:
            right_sum = find_sum_of_path_helper(
                root.right, val_so_far + str(root.val))
        return left_sum + right_sum


def find_sum_of_path_numbers(root):
    return _traverse(root, 0)


def _traverse(root, total_sum, path=None):
    if path is None:
        path = []

    path.append(root.val)

    if root.left is None and root.right is None:
        # two version for converting multiple integer of a list to single
        # integer.
        total_sum += int(''.join(str(i) for i in path))
        # total_sum += int(''.join(map(str, path)))
    else:
        total_sum = _traverse(root.left, total_sum, path)
        total_sum = _traverse(root.right, total_sum, path)

    path.pop()

    return total_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
