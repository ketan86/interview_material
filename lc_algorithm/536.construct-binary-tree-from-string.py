"""
536. Construct Binary Tree from String
Medium

672

116

Add to List

Share
You need to construct a binary tree from a string consisting of parenthesis
and integers.

The whole input represents a binary tree. It contains an integer followed by
zero, one or two pairs of parenthesis. The integer represents the root's value
and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it
exists.


Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        """

                2
            3       1

            2(3)(1)
            ^ 

            node_value = 2
            node = TreeNode(2)
            found '('
                node.left = {        
                    2(3)(1)
                       ^
                      node_value = 3
                      node = TreeNode(3)
                      found ')'
                        node.right = {
                            2(3)(1)
                                  ^
                                node_value = 1
                                node = TreeNode(1)
                                node.right = {
                                    return none
                                } = None
                        } = 1
                } = 3


        """
        if not s:
            return
        n = len(s)
        self.index = 0

        def build():
            # build number
            start = self.index
            while self.index < n and s[self.index] not in '()':
                self.index += 1

            num = s[start:self.index]
            if num:
                node = TreeNode(int(num))
            else:
                node = None

            # go left
            if self.index < n and s[self.index] == '(':
                self.index += 1
                node.left = build()
            # go left
            if self.index < n and s[self.index] == '(':
                self.index += 1
                node.right = build()
            # go right
            if self.index == n or s[self.index] == ')':
                self.index += 1
                return node

        return build()

    def str2treeIterative(self, s: str) -> TreeNode:
        """Runtime: 252 ms, faster than 12.23%
        """
        if not s:
            return

        root = None
        node_value = ''
        stack = []
        for index, char in enumerate(s):
            if not root and char not in '()':
                node_value += char

            elif char == '(':
                if not root:
                    root = TreeNode(int(node_value))
                stack.append(index)

            elif char == ')':
                tree_start_index = stack.pop()
                if not stack:
                    if not root.left:
                        root.left = self.str2tree(s[tree_start_index+1: index])
                    else:
                        root.right = self.str2tree(s[tree_start_index+1:index])

        if not root:
            root = TreeNode(int(node_value))

        return root


print(Solution().str2tree("2(3)(1)"))
