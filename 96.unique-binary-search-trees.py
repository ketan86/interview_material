#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (47.33%)
# Likes:    2780
# Dislikes: 105
# Total Accepted:    262.7K
# Total Submissions: 522K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# @lc code=start


class Solution:
    """
    n |nodes| unique trees
    0  {}     1   -> hypothetically assume null tree is one tree.
    1  {1}    1   -> make 1 as root, we can only make one tree.
    2  {1,2}  2   -> make 1 as root, on the left there are no nodes
                     but only the right there is one node (2).
                     or make 2 as a root and there is a one node on
                     the left and no one on the right.

                      1         +        2
                    /   \              /   \
                   {}   {2}          {1}     {}
                n=0(1) * n=1(1) + n=1(1) * n=0(1) = 2 BST

    3  {1,2,3} 5  -> make 1, 2 and 3 as root node so,
                      1         +        2            3 
                    /   \              /   \        /   \
                   {}    {2,3}       {1}    {3}    {1,2} {}
                n=0(1) * n=2(2) + n=1(1) * n=1(1) + n=2(2) *n=0{1} = 5 BST

                   j      i-j-1      j                j
                   0      3-0-1=2
    To derive the formula,
        1. iterate over the each node as i for each root.
        2. for each node, iterate over from 0 to ith node and add all the
           combinations.
    """

    def numTrees(self, n):
        # set number of bst's to 0 from 0..n+1
        dp = [0] * (n + 1)
        # for tree with 0 node, hypothetically we can assume we can have
        # 1 (null) unique tree possible.
        dp[0] = 1
        # for 1 node, 1 BST
        dp[1] = 1
        # from 2..n+1 node
        for i in range(2, n + 1):
            # run j from 0..i and find all BST's and sum it up.
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        # return total BST's at index n.
        return dp[n]


# print(Solution().numTrees(3))
# @lc code=end
