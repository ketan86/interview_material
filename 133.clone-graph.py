#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (32.73%)
# Likes:    1514
# Dislikes: 1280
# Total Accepted:    313.1K
# Total Submissions: 952.2K
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.
#
#
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
#
#
#
#
# Test case format:
#
# For simplicity sake, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val = 1, the second node with
# val = 2, and so on. The graph is represented in the test case using an
# adjacency list.
#
# Adjacency list is a collection of unordered lists used to represent a finite
# graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
#
#
# Example 2:
#
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
#
#
# Example 3:
#
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
#
#
# Example 4:
#
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
#
#
#
# Constraints:
#
#
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
#
#
#

# @lc code=start
# pylint: skip-file
# Definition for a Node.
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        return self.dfs(node)

    def dfs(self, root):
        # visited dict to store the visited node and respective clone.
        visited = {}

        queue = deque()
        queue.append(root)
        # add root node to visited with clone copy. neighbors are still
        # not explored so it will be added later on.
        visited[root] = Node(root.val, [])

        while queue:
            # pop the node from the queue
            node = queue.popleft()
            # visit all non-visited neighbors
            for neighbor in node.neighbors:
                # if node not visted
                if neighbor not in visited:
                    # add neighbor to a visited node with a clone copy.
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # add neighbor to a neighbors list of current node.
                visited[node].neighbors.append(visited[neighbor])

        # return root of clone
        return visited[root]


g = Node(
    1, [
        Node(
            2, [
                Node(1, []), Node(
                    3, [
                        Node(2, []), Node(4, [])
                    ]
                )]
        ),
        Node(
            4, [
                Node(1, []), Node(3, [])]
        ),
    ])

# new_graph = Solution().cloneGraph(g)
# import pdb;pdb.set_trace()
# @lc code=end
