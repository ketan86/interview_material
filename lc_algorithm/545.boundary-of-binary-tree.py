"""
545. Boundary of Binary Tree Medium

801

1354

Add to List

Share The boundary of a binary tree is the concatenation of the root, the left
boundary, the leaves ordered from left-to-right, and the reverse order of the
right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a
left child, then the left boundary is empty. If a node in the left boundary and
has a left child, then the left child is in the left boundary. If a node is in
the left boundary, has no left child, but has a right child, then the right
child is in the left boundary. The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side
of the root's right subtree. Again, the leaf is not part of the right boundary,
and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root
is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Example 1:


Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
Example 2:


Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4.
  4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
  10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000

"""
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
    [1,2,null,3,null,4]
    
            1
        /     \ 
       2       4
      /
     3          

"""


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):

        def find_left_boundary_nodes(node, ls):
            if node:
                # check first left and no left, go right and check left of that
                if node.left:
                    ls.append(node.val)
                    find_left_boundary_nodes(node.left, ls)
                elif node.right:
                    ls.append(node.val)
                    find_left_boundary_nodes(node.right, ls)

        def find_right_boundary_nodes(node, ls):
            if node:
                # check right and if no right, go left and check right of that
                if node.right:
                    ls.appendleft(node.val)
                    find_right_boundary_nodes(node.right, ls)
                elif node.left:
                    ls.appendleft(node.val)
                    find_right_boundary_nodes(node.left, ls)

        def find_leaf_nodes(node, ls):
            if node:
                # if not left and right, its a leaf node
                if not node.left and not node.right:
                    ls.append(node.val)
                else:
                    # find left nodes on left and right
                    find_leaf_nodes(node.left, ls)
                    find_leaf_nodes(node.right, ls)

        # if root is none, return empty list
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:

            left_boundary_nodes = []
            right_boundary_nodes = collections.deque()
            leaf_nodes = []

            find_left_boundary_nodes(root.left, left_boundary_nodes)
            find_right_boundary_nodes(root.right, right_boundary_nodes)
            find_leaf_nodes(root, leaf_nodes)

            return [root.val] + left_boundary_nodes + leaf_nodes + list(right_boundary_nodes)
