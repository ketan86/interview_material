"""
428. Serialize and Deserialize N-ary Tree Hard

662

37

Add to List

Share Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is
a rooted tree in which each node has no more than N children. There is no
restriction on how your serialization/de-serialization algorithm should work. You
just need to ensure that an N-ary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree


 

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not
necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format,
where each group of children is separated by the null value.


 

For example, the above tree may be serialized as
[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

 

Example 1:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Example 2:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
"""
# Definition for a Node.

# Definition for a Node.


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: Node) -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []
        if not root:
            return ""

        def dfs(root):
            res.append(str(root.val))
            res.append(str(len(root.children)))
            if len(root.children) == 0:
                return
            for child in root.children:
                dfs(child)

        dfs(root)

        return " ".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        ls = data.split(' ')
        if len(ls) < 2:
            return None
        idx = 0

        def dfs():
            nonlocal idx

            if idx >= len(ls):
                return None
            node = Node(int(ls[idx]))
            idx += 1
            num_child = int(ls[idx])
            idx += 1
            node.children = []

            for _ in range(num_child):
                node.children.append(dfs())

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
