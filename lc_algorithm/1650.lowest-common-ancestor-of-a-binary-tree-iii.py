"""
1650. Lowest Common Ancestor of a Binary Tree III Medium

242

8

Add to List

Share Given two nodes of a binary tree p and q, return their lowest common
ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is
below:

class Node {public int val; public Node left; public Node right; public Node
    parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of
two nodes p and q in a tree T is the lowest node that has both p and q as
descendants (where we allow a node to be a descendant of itself)."


Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
Accepted
26,353
Submissions
34,302
"""
# Definition for a Node.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Runtime: 80 ms, faster than 22.70%

                    p
                /       \
               q    or   q

                    q
                /       \
                p        p

                    root
                    |
                    x
                  /  \
                 p    x
                     /  \
                    q    x
        """
        # Choose any node and find the tree root
        root = p
        while root.parent:
            root = root.parent

        # Find lca from the root
        def find_lca(node, p, q):
            if not node:
                return

            if node.val == p.val or node.val == q.val:
                return node

            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)

            if left and right:
                return node

            if left:
                return left

            if right:
                return right

        return find_lca(root, p, q)

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Solution: using space
        path = set()
        while p:
            path.add(p.val)
            p = p.parent

        while q:
            if q.val in path:
                return q
            q = q.parent

        return None

        # Solution: modifies a tree
        # # First, we remove all parent links in the path from p to the root.
        # while p.parent:
        #     p.parent, p  = None, p.parent

        # # Then, we go up while there is a parent link. When there isn't anymore, we've found the common ancestor.
        # while q.parent:
        #     q = q.parent

        # return q
