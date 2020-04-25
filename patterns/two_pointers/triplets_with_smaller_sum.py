"""
Given an array arr of unsorted numbers and a target sum, count all triplets
in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
different indices. Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target:
[-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""
# pylint: skip-file


# Big(O) - N^3
def triplet_smaller_sum(arr, target_sum):
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum_ = arr[i] + arr[j] + arr[k]
                if sum_ < target_sum:
                    count += 1
                else:
                    break
    return count

# Big(O) - N^2


def triplet_smaller_sum(arr, target_sum):
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            sum_ = arr[i] + arr[j] + arr[k]
            if sum_ < target_sum:
                # trick : if we find the number where sum is less than target,
                # all the numbers between j and k are all also less than
                # target in sorted array.
                count += k - j
                j += 1
            else:
                k -= 1
    return count

# Big(O) - N^3


def triplet_smaller_sum_results(arr, target_sum):
    triplets = []
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            sum_ = arr[i] + arr[j] + arr[k]
            if sum_ < target_sum:
                m = j
                n = k
                # when a sum is less than target, all elements from k to j
                # are all with sum less than target.
                while m < n:
                    triplets.append([arr[i], arr[m], arr[n]])
                    n -= 1
                j += 1
            else:
                k -= 1
    return triplets


# print(triplet_smaller_sum([-1, 4, 2, 1, 3], 5))
print(triplet_smaller_sum_results([-1, 4, 2, 1, 3], 5))
