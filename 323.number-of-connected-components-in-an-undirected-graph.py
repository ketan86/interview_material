#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (54.87%)
# Likes:    830
# Dislikes: 25
# Total Accepted:    107.4K
# Total Submissions: 190.3K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
#
# Example 1:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
#
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
#
# Output:  1
#
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
#

# @lc code=start
from collections import deque


class Solution:
    def countComponents(self, n, edges):
        """
        Following scenarios must be considered.

        1. single non connected node
        2. all nodes are connected
        3. more than one graph
        """
        # create a undirected graph
        graph = {i: [] for i in range(n)}
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        # queue for bfs
        queue = deque()
        conn_nodes = 0
        # mark all nodes unvisited.
        visited = [False] * n

        # 1. in undirected graph, one can chose to pick any node and traverse
        # until all nodes in that graph is visited.
        # 2. if there are graphs with more than one node, those nodes
        # won't be visited in step 1. so by checking the non visited node, we
        # can find another graph.
        # 3. if node is not connected (no child), we still have to visited that
        # node and consider that a graph with one node.

        # loop until all nodes are not visited.
        while not all(visited):
            # find the first non visited node
            non_visited_node = visited.index(False)
            # IMP: mark it visited.
            visited[non_visited_node] = True
            # add it to queue with parent set to -1
            queue.append((non_visited_node, -1))

            # dfs
            while queue:
                node, parent = queue.popleft()
                # if node is not a parent (backedge). if undirected
                # graph, we have to ensure the backedge is not visited
                # to avoid infinite looping.
                if node != parent:
                    for child in graph[node]:
                        if not visited[child]:
                            visited[child] = True
                            # append child with node being it's parent.
                            queue.append((child, node))

            # we have completed traversing the whole graph, so increment the
            # count.
            conn_nodes += 1

        return conn_nodes

# @lc code=end
