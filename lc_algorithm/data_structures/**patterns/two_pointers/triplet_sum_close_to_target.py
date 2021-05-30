"""

Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1 
Output: 2 
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3 -10^3 <= nums[i] <= 10^3 -10^4 <= target <= 10^4

"""
# pylint: skip-file


# Big(O) - N^3
def triplet_sum(arr, target_sum):
    arr.sort()
    n = len(arr)
    lowest_sum = [float('inf'), float('inf')]
    running_diff = float('inf')
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum_ = arr[i] + arr[j] + arr[k]
                diff = abs(sum_ - target_sum)
                running_diff = min(running_diff, diff)
                if running_diff == diff:
                    if lowest_sum[1] == diff:
                        lowest_sum[0] = min(lowest_sum[0], sum_)
                    else:
                        lowest_sum[0] = sum_
                    lowest_sum[1] = diff

    if lowest_sum == float('inf'):
        return None
    return lowest_sum[0]

# Big(O) - N^2


def triplet_sum(arr, target_sum):
    """
    In this problem, we either find the triplet with sum equal to target
    or less than the target. If we find equal to target, we can return
    else we have to update the the smallest sum by maintaining the running sum.
    """
    # sort the array to make it efficient.
    arr.sort()
    n = len(arr)
    # set smallest diff to infinite number so first number would
    # be considered the smallest comapre to this value.
    running_smallest_diff = float('inf')
    # loop over the array until last two elements(due to triplet)
    for i in range(n - 2):
        # use left and right indexes to find the sum that is equal to
        # target and move indexes based on the target sum.
        left = i + 1
        right = n - 1
        # iterate from left to right
        while left < right:
            # find the sum
            sum_ = arr[i] + arr[left] + arr[right]
            diff = target_sum - sum_
            # if sum is  equal to target, return the sum
            if diff == 0:
                return sum_
            # if diff less than the current running smallest diff,
            # update smallest running diff to new diff
            if abs(diff) < abs(running_smallest_diff):
                running_smallest_diff = diff

            # if diff is greater than 0, move left else right
            if diff > 0:
                left += 1
            else:
                right -= 1

    # return the sum
    return target_sum - running_smallest_diff


print(triplet_sum([-2, 0, 1, 2], 2))
