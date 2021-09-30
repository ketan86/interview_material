#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
"""
373. Find K Pairs with Smallest Sums Medium

2164

142

Add to List

Share You are given two integer arrays nums1 and nums2 sorted in ascending order
and an integer k.

Define a pair (u, v) which consists of one element from the first array and one
element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 104
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 1000
Accepted
136,597
Submissions
351,217

"""
# @lc code=start
import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        K smallest pairs in sorted arrays won't be more than k elements
        in each array.
        """
        # max heap to maitain sum, and pair
        max_heap = []
        # go till min or k or nums1 and num2
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                sum_ = nums1[i] + nums2[j]
                # till k elements, put all the pairs
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-sum_, nums1[i], nums2[j]))
                elif sum_ < -max_heap[0][0]:
                    heapq.heapreplace(max_heap, (-sum_, nums1[i], nums2[j]))
                else:
                    # if sum is greater than top element, due to sorted
                    # nature of the arrays, we will not find any smaller
                    # elements going forward so break.
                    break

        # build results and return.
        results = []
        while max_heap:
            sum_, i, j = heapq.heappop(max_heap)
            results.append([i, j])

        return results


# @lc code=end
