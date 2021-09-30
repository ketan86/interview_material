#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecBFS:
    """Runtime: 112 ms, faster than 79.77% of"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node:
                result.append('None')
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        [1,2,3,null,null,4,5,6,7]


        """
        if not data:
            return
        nodes = data.split(',')

        # build rood node using the first node value
        root = TreeNode(int(nodes[0]))
        # put root node in queue and iterate over the queue to find all
        # child nodes
        queue = deque()
        queue.append(root)

        # use pointer to go over all the nodes instead of using equation
        # like (root * 2) + 1  -> left and (root *2) + 2 -> right
        i = 1

        while i < len(nodes) and queue:
            # extract root
            node = queue.popleft()
            # if not None, then create a node and assign to left of the root
            # also put that in queue
            if nodes[i] != 'None':
                left = TreeNode(int(nodes[i]))
                node.left = left
                queue.append(left)

            # increment the
            i += 1
            if nodes[i] != 'None':
                right = TreeNode(int(nodes[i]))
                node.right = right
                queue.append(right)
            i += 1

        return root


class CodecDFS:
    """SLOWER: Runtime: 188 ms, faster than 20.18%"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        : type root: TreeNode
        : rtype: str
        """
        if not root:
            return

        def dfs(node, s):
            if not node:
                s += 'None,'
            else:
                s += str(node.val) + ','
                s = dfs(node.left, s)
                s = dfs(node.right, s)
            return s

        return dfs(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        : type data: str
        : rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(',')

        def dfs(nodes):
            if nodes[0] == 'None':
                nodes.pop(0)
                return
            else:
                root = TreeNode(nodes[0])
                nodes.pop(0)
                root.left = dfs(nodes)
                root.right = dfs(nodes)
            return root

        return dfs(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
