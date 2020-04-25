"""
Problem Statement #
Given an array of unsorted numbers, find all unique triplets that are close 
to target sum.

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
    arr.sort()
    n = len(arr)
    smallest_diff = float('inf')
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            sum_ = arr[i] + arr[left] + arr[right]
            diff = target_sum - sum_
            if diff == 0:
                return target_sum - diff
            if abs(diff) < abs(smallest_diff):
                smallest_diff = diff

            if diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_diff


print(triplet_sum([-2, 0, 1, 2], 2))
