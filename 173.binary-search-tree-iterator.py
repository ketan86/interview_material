#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (49.94%)
# Likes:    2179
# Dislikes: 265
# Total Accepted:    281.4K
# Total Submissions: 518.5K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
#  '[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# pylint: skip-file

class BSTIterator:
    
    def __init__(self, root):
        self.root = root
        # create an iterator from the dfs method.
        self.iterator = self.dfs(self.root)
        # variable to hold the next item for has_next method.
        # we have to retrive an item in order to find if iterator
        # has next value or not. this item is stored and returned
        # as a first item when next item is retrieved.
        self.next_item = None
        
    def __iter__(self):
        return self

    def hasNext(self):
        # every hasNext call does not pull item from the iterator.
        # if we have an item, we return true all the time for this
        # call
        if self.next_item:
            return True

        # if we do not have an item, pull a new item, store it and
        # return true. if we dont have an item, return false.
        try:
            self.next_item = next(self.iterator)
        except StopIteration:
            return False
        else:
            return True

    def next(self):
        # if we have already pulled one item, return that first before
        # pulling a new item.
        if self.next_item:
            value = self.next_item
            # reset next item to None so we do not return the same item again.
            self.next_item = None
            return value
        
        # pull a new item and return the value.
        try:
            return next(self.iterator)
        except StopIteration:
            pass

    def dfs(self, node):
        # iterate over the nodes until it's none.
        if node is not None:
            # yield from is required because, recursive call to the same
            # function returns a new generator.
            yield from self.dfs(node.left)
            # yield a node value
            yield node.val
            # same for right node
            yield from self.dfs(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @lc code=end
