#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#

# @lc code=start
import collections


class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        graph = collections.defaultdict(set)
        max_network_rank = 0

        # create bi-directional graph
        for x, y in roads:
            graph[x].add(y)
            graph[y].add(x)

        # defaultdict(<class 'set'>, {0: {1, 3}, 1: {0, 2, 3}, 3: {0, 1}, 2: {1}})
        # compare two cities and find the total edges that are connected to
        # both cities excluding the direct one (if there is any)

        # city(0, 1) -> 5 - 1(direct) = 4
        # city(1, 2) -> 4 - 1(direct) = 3
        # city(2, 3) -> 3 - 0(direct) = 3
        # city(0, 2) -> ...

        for i in range(n):
            for j in range(i + 1, n):
                # count the edges excluding the direct edge
                cnt = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    cnt -= 1
                # track the maximum edges
                max_network_rank = max(max_network_rank, cnt)

        return max_network_rank


print(Solution().maximalNetworkRank(
    n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))
# @lc code=end
