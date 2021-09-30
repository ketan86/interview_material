#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#
"""
1359. Count All Valid Pickup and Delivery Options
Hard

337

39

Add to List

Share
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is
always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90


Constraints:

1 <= n <= 500
Accepted
14,141
Submissions
25,359
"""
# @lc code=start


class Solution:
    def countOrders(self, n: int) -> int:
        """
        Since each order has a pick-up and deliver, imagine 2N empty slots in
        which we can assign a pickup or a delivery for any of the orders.

        Now think about the first slot. This slot, no matter what, has to be a pickup.
        So for the first slot, we have N choices. Now, we have 2N-1 remaining slots. The
        trick is to see that we can actually reduce the problem to a problem with N-1
        orders by noting that in any of the 2N-1 slots, we can put in the delivery
        corresponding to the first pickup. Then the remaining 2N-2 slots can be treated
        as the problem with N-1 remaining pickups and deliveries!

        So the recursion is just dp[n] = N*(2N-1)*dp[n-1]

        """
        # seems like a math problem
        MOD = 10**9+7

        def count(n):
            if n == 1:
                return 1
            else:
                return ((n * (2*n-1)) * count(n-1)) % MOD

        return count(n)

    def countOrders(self, n: int) -> int:
        res = set()
        visited = set()

        def backtrack(path=[]):

            if len(path) == n*2:
                res.add(tuple(path))
            else:
                for i in range(1, n+1):
                    if i not in visited:
                        visited.add(i)
                        backtrack(path + ["P" + str(i)])
                        visited.discard(i)

                    if i in visited and -1*i not in visited:
                        visited.add(-1*i)
                        backtrack(path + ["D" + str(i)])
                        visited.discard(-1*i)
        backtrack()
        return len(res)
# @lc code=end
