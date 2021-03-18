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
    # store results
    all_paths = []
    # traverse the tree from root and save paths
    _traverse(root, all_paths)
    # return the paths
    return all_paths


def _traverse(root, all_paths, path=None):
    """
    Traverse the node and if leaf node is found, backtrack.
    for ex,
                      1
                  /      \
                2         3
            /      \   /    \
           4       5  6      7

        path = []
            1. add root 1 -> [1]
            2. go left, left, left for dfs
            3  add root 4 -> [1,2,4]
            4. no left or right child so it's a leaf
                add copy of the current path to result
            5. backtrack by removing 4 from the path
            6. now root is 2 -> [1,2]
            7. go to left
            8. now root is 5 -> [1,2,5]
            9. no left and right child so it's a leaf
                add copy of the current path to result
            10. backtrack by removing 5 from the path
            11. backtrack bu removing 2 from the path
            12. now root is 3 -> [1,3]
            13. go to left
            ...
    """
    # **NOTE*: Never set path=[] empty list in the args. It will yield unexpected results

    # if path is None, set to empty list
    if path is None:
        path = []

    # if root node is none, return
    if root is None:
        return

    # add root node to path
    path.append(root.val)

    # find a leaf node where both left and right child are none.
    if not root.left and not root.right:
        # instead of appending the path (which only references the list)
        # copy the list using the list func.
        all_paths.append(list(path))

    # no need to check since we are returning if root is none.
    _traverse(root.left, all_paths, path)
    _traverse(root.right, all_paths, path)

    # pop the node that was added to path
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
