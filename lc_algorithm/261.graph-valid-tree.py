#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (41.53%)
# Likes:    1103
# Dislikes: 38
# Total Accepted:    135.8K
# Total Submissions: 320.6K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
#
# Example 1:
#
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
#
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    # def validTree(self, n, edges):
    #     g = defaultdict(list)

    #     for p, c in edges:
    #         g[p].append(c)
    #         g[c].append(p)

    #     # define all nodes to not visited
    #     visited = [False] * len(g)

    #     # if there are cycles, it is not a tree.
    #     for node in g.keys():
    #         if self._has_cycle(g, node, visited, -1):
    #             return False

    #     # if all nodes are not visited, it's not a tree.
    #     return all(visited)

    # def _has_cycle(self, g, node, visited, parent):
    #     # mark node visited
    #     visited[node] = True
    #     # get head and traverse.
    #     for child in g[node]:
    #         # if not visited, check for cycle
    #         if not visited[child]:
    #             if self._has_cycle(g, child, visited, node):
    #                 return True
    #         # if visited and not the parent, If node is parent, we can't
    #         # consider it a loop.
    #         elif child != parent:
    #             return True
    #     return False

    def validTree(self, n, edges):
        """
            0
        /   |   \
       1    2   3
       |
       4


       defaultdict(<class 'list'>, {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]})

       visited = { 0: -1 } -> node, parent
       queue(0)
            -> item -> 0 (node)
                    child -> 1,2,3
                        1 == 0 (child == parent) (skip)
                        1 in visited -> yes (break return False)

                        put 1 in visited with parent 0
                        put 1 in queue

       """

        # node value should be 1 less than the edges.
        if len(edges) != n - 1:
            return False

        # adjacency list
        adj_list = defaultdict(list)

        # bidirectional edges
        for p, c in edges:
            adj_list[p].append(c)
            adj_list[c].append(p)

        # maintain visited and parent node
        visited = {0: -1}
        # put first node into the queue
        queue = deque([0])

        while queue:
            node = queue.popleft()
            # iterate over the neighbors
            for child in adj_list[node]:
                # if child is not visited, put it in queue
                if child not in visited:
                    visited[child] = node
                    queue.append(child)
                else:
                    # if child visited and not parent, we found a cycle
                    parent = visited[node]
                    if child != parent:
                        return False

        # if not all visited (disconnected graph)
        return len(visited) == n


print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))


# @lc code=end
