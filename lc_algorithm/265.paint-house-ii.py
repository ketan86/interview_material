# Hard

# There are a row of n houses, each house can be painted with one of the **k
# colors**. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the
# same color.

# The cost of painting each house with a certain color is represented by an n x
# k cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with color 0
# costs[1][2] is the cost of painting house 1 with color 2, and so on... Return
# the minimum cost to paint all houses.


# Example 1:

# Input: costs = [[1, 5, 3], [2, 9, 4]]
# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Example 2:

# Input: costs = [[1, 3], [2, 4]]
# Output: 5


# Constraints:

# costs.length == n
# costs[i].length == k
# 1 <= n <= 100
# 1 <= k <= 20
# 1 <= costs[i][j] <= 20


# Follow up: Could you solve it in O(nk) runtime?

class Solution:  # O(n * k)
    """
    Naive Solution: calculate min of all the previous houses for each color
    except same previous index. O(n * k * k) 

    Runtime: 100 ms, faster than 90.83%

    """

    # O(n * k)
    # O(1)
    def minCostII(self, costs): 
        # if no house, no point
        if not costs:
            return 0

        # go over all the house starting from second
        for house in range(1, len(costs)):
            # first min to use for all the house except current house
            first_min = min(costs[house-1])
            first_min_index = costs[house-1].index(first_min)

            # second min to use for current house
            second_min = min(
                costs[house-1][:first_min_index] + costs[house-1][first_min_index+1:])

            # go over the all paint options
            for color_index in range(len(costs[house])):
                # if color is same, use second min cost else first min_cost
                if first_min_index == color_index:
                    costs[house][color_index] += second_min
                else:
                    costs[house][color_index] += first_min

        # return the min of the final cost accumulated over time.
        return min(costs[-1])
