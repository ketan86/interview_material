#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#
# https://leetcode.com/problems/find-the-celebrity/description/
#
# algorithms
# Medium (40.81%)
# Likes:    997
# Dislikes: 127
# Total Accepted:    117.2K
# Total Submissions: 286.9K
# Testcase Example:  '[[1,1,0],[0,1,0],[1,1,1]]'
#
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among
# them, there may exist one celebrity. The definition of a celebrity is that
# all the other n - 1 people know him/her but he/she does not know any of
# them.
#
# Now you want to find out who the celebrity is or verify that there is not
# one. The only thing you are allowed to do is to ask questions like: "Hi, A.
# Do you know B?" to get information of whether A knows B. You need to find out
# the celebrity (or verify there is not one) by asking as few questions as
# possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A
# knows B. Implement a function int findCelebrity(n). There will be exactly one
# celebrity if he/she is in the party. Return the celebrity's label if there is
# a celebrity in the party. If there is no celebrity, return -1.
#
#
#
# Example 1:
#
#
# Input: graph = [
# [1,1,0],
# [0,1,0],
# [1,1,1]
# ]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1
# means person i knows person j, otherwise graph[i][j] = 0 means person i does
# not know person j. The celebrity is the person labeled as 1 because both 0
# and 2 know him but 1 does not know anybody.
#
#
# Example 2:
#
#
# Input: graph = [
# [1,0,1],
# [1,1,0],
# [0,1,1]
# ]
# Output: -1
# Explanation: There is no celebrity.
#
#
#
#
# Note:
#
#
# The directed graph is represented as an adjacency matrix, which is an n x n
# matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0
# means the contrary.
# Remember that you won't have direct access to the adjacency matrix.
#
#
#

# @lc code=start
# pylint: skip-file


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:

    # O(n^2) solution
    def findCelebrity(self, n: int) -> int:
        # NOTE: CHECK THE VALIDITY OF THIS SOLUTION -> WHY RETURN -1 EARLY
        # store the total number of people knows the person in array
        for celebrity in range(n):
            for person in range(n):
                if celebrity == person:
                    continue
                if knows(celebrity, person) or not knows(person, celebrity):
                    return - 1
                else:
                    return celebrity
        return -1

        """
        NOTE: IS THIS NOT RIGHT INSTEAD ?

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(j, i) and not knows(i, j):
                    break
            else:
                return i
        return -1
        """

    # O(n) solution

    def findCelebrity(self, n: int) -> int:
        # consider first person a celebrity
        candidate = 0
        # if candidate knows the other person, he/she can not be a celebrity.
        # may be the other person could be celebrity.
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        # once we find the celebrity candidate, check if candidate if truly
        # by checking if candidate knows other person but other person does
        # not know candidate. return -1 if that check fails.
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return - 1

        return candidate


# @lc code=end
