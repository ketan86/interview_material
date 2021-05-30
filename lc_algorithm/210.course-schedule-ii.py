#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque


class Solution:
    def findOrder(self, num_courses, prerequisites):
        """
        Runtime: 104 ms, faster than 33.19%

        Steps:
        1. Initialize courses list to store courses visited during
            traversal.
        2. Define graph and in_degree map to store relationships.
        3. Iterate over the given prereq list and populate graph
            and in_degree map.
        4. Fill queue with courses that are not dependent on
            any other course.
        5. Iterate over the queue and reduce the in_degree for each
            child node visited. Put node with in_degree to 0 in queue.
        6. Fill courses list during the traversal.
        7. Return courses list (one of the ordering)
        """

        # store courses during traversal
        courses = []

        in_degree = {i: 0 for i in range(num_courses)}
        graph = {i: [] for i in range(num_courses)}

        # create graph and in_degree map
        for p in prerequisites:
            p2, p1 = p
            graph[p1].append(p2)
            in_degree[p2] += 1

        # find courses that are not dependent on any other courses
        sources = deque()

        for k, v in in_degree.items():
            if v == 0:
                sources.append(k)

        # iterate over the source
        while sources:
            node = sources.popleft()
            courses.append(node)
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if all courses are not iterated, there is no ordering possible
        if len(courses) != num_courses:
            return []

        return courses


print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution().findOrder(1, []))


# @lc code=end
