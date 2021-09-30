"""

510. Inorder Successor in BST II Medium

514

27

Add to List

Share Given a node in a binary search tree, return the in-order successor of
that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each
node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
 

Follow up: Could you solve it without looking up any of the node's values?

Accepted
34,363
Submissions
56,515

"""
# Definition for a Node.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: Node) -> Node:
        """Runtime: 96 ms, faster than 11.27%"""
        """
                2
              /   \
             1     33  <-- node (34 successor)  1 right and all the way left
                 /    \
                25     40
                      /
                     34
        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left

            return node

        """
                    25  <- successor
                  /
                 11
               /   \
              7     12
                      \
                       13 <-- node (keep going parent until node.right != parent, parent is successor)

                       null
                       |
                       2
                      /  \
                    1      33
                          /   \
                         25    40 <-- node (null successor)
                              /
                             34  <-- node (40 successor)
        """
        while node.parent and node == node.parent.right:
            node = node.parent

        return node.parent
