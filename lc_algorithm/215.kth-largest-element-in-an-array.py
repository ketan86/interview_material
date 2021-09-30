#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (53.49%)
# Likes:    3327
# Dislikes: 232
# Total Accepted:    580.7K
# Total Submissions: 1.1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
#
# Example 2:
#
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
#

# @lc code=start
# pylint:skip-file
import heapq


class Solution:

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)

    # O(nlogn) solution

    def findKthLargest(self, nums, k):
        # sort and return the kth element from end
        nums.sort()
        return nums[len(nums)-k]

    # O(nlogk) solution  ---> Better than above
    def findKthLargest(self, nums, k):
        """Runtime: 68 ms, faster than 50.12%"""
        # min heap to store the max k largest elements
        min_heap = []

        for i in nums:
            # store first k elements
            if len(min_heap) < k:
                heapq.heappush(min_heap, i)
            else:
                # if top element is less than the current element,
                # replace it with current element
                top = min_heap[0]
                if i > top:
                    heapq.heapreplace(min_heap, i)

        # top element is the kth largest. peek or pop
        return min_heap[0]
        # or return heapq.heappop(min_heap)

# @lc code=end
