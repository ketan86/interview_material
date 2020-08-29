#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (40.37%)
# Likes:    1121
# Dislikes: 119
# Total Accepted:    64.8K
# Total Submissions: 157.8K
# Testcase Example:  '[5,10,-5]'
#
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions.  If two asteroids
# meet, the smaller one will explode.  If both are the same size, both will
# explode.  Two asteroids moving in the same direction will never meet.
#
#
# Example 1:
#
# Input:
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation:
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
#
#
#
# Example 2:
#
# Input:
# asteroids = [8, -8]
# Output: []
# Explanation:
# The 8 and -8 collide exploding each other.
#
#
#
# Example 3:
#
# Input:
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation:
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in
# 10.
#
#
#
# Example 4:
#
# Input:
# asteroids = [-2, -1, 1, 2]
# Output: [-2, -1, 1, 2]
# Explanation:
# The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet
# each other.
#
#
#
# Note:
# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..
#
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        # if there are no asteroids, return empty list.
        if not asteroids:
            return stack
        # iterate over the asteroid list
        for asteroid in asteroids:
            # if it's a first asteroid, save it.
            if not stack:
                stack.append(asteroid)
            else:
                # unless the stack is empty, run the loop
                while stack:
                    # if prev astroid is moving in right side (+) and
                    # current in left direction (-), collision is possible.
                    if stack[-1] > 0 and asteroid < 0:
                        # three possibilities
                        # 2: prev asteroid is smaller than curr (prev explodes)
                        # check the stack and repeat the process.
                        # NOTE: if stack is empty after this condition,
                        # we have to add the curr asteroid in the stack.
                        # while -> else condition takes care of that.
                        if stack[-1] < -asteroid:
                            stack.pop()
                        # 2: prev asteroid is bigger than curr (curr explodes)
                        # go to next astroid
                        elif stack[-1] == -asteroid:
                            stack.pop()
                            break
                        # 3: prev asteroid is less than curr (prev explodes)
                        else:
                            break
                    # if pre astroid is moving in left side (-) and current
                    # in right direction (+) or both in either left or right,
                    # collision is not possible, save the asteroid.
                    else:
                        stack.append(asteroid)
                        break
                # if stack got empty and curr asteroid destroys all the
                # asteroids from the stack, curr asteroid must be added
                # in the stack.
                else:
                    stack.append(asteroid)
        return stack


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
print(Solution().asteroidCollision([-2, 1, -1, 2]))
# @lc code=end
