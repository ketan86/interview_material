#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# O(n^3)


# class Solution:
#     def threeSum(self, nums):
#         results = []
#         n = len(nums)
#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         sum_pair = [nums[i], nums[j], nums[k]]
#                         for result in results:
#                             if sorted(sum_pair) == sorted(result):
#                                 break
#                         else:
#                             results.append(sum_pair)
#         return results


# O(n^2)
class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i == 0 or nums[i] > nums[i - 1]:
                low = i + 1
                high = n - 1
                expected_sum = -nums[i]
                while low < high:
                    sum_ = nums[low] + nums[high]
                    if sum_ == expected_sum:
                        results.append([nums[i], nums[low], nums[high]])
                    if sum_ > expected_sum:
                        current_high = high
                        while (nums[high] == nums[current_high] and low < high):
                            high -= 1
                    else:
                        current_low = low
                        while (nums[low] == nums[current_low] and low < high):
                            low += 1
        return results


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([-2, 0, 0, 2, 2]))
