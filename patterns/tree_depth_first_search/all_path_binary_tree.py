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
    all_paths = []
    _traverse(root, all_paths)
    return all_paths


def _traverse(root, all_paths, path=None):
    if path is None:
        path = []
    if root is None:
        return

    path.append(root.val)
    
    if root.left is None and root.right is None:
        all_paths.append(list(path))

    _traverse(root.left, all_paths, path)
    _traverse(root.right, all_paths, path)

    path.pop()


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree paths: " + str(find_paths(root)))


main()
