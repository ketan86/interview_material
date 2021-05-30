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


# def _total_sum_(root, sum_=0):
#     # if not root node, return the current sum
#     if not root:
#         return sum_
#     # if leaf node, return the sum by adding root value to it
#     if not root.left and not root.right:
#         return sum_ + root.val

#     # return the sum of left and right subtree.
#     return _traverse(root.left, sum_ + root.val) + _traverse(root.right, sum_ + root.val)


def find_sum_of_path_numbers(root):
    return _traverse(root, 0)


def _traverse(root, total_sum, path=None):

    # if path is None, set it to []
    if path is None:
        path = []

    # if root is None, return total sum
    if not root:
        return total_sum

    # add root to path
    path.append(root.val)

    # if leaf node, create integer by concatinating the individual
    # integers into a string and later adding it to total sum
    if not root.left and not root.right:
        total_sum += int(''.join(str(i) for i in path))

    # find total sum of left and right subtree
    total_sum = _traverse(root.left, total_sum, path)
    total_sum = _traverse(root.right, total_sum, path)

    # remove the root node
    path.pop()

    # return the total sum
    return total_sum


def main():
    # 408 total sum
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
