"""
Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add
up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

# three pointer problem.
1. sort array to find sum easily. in sorted array, you can move two pointers
close to each other based on the whether the sum comes out to be greater or
less than 0.
        i    m               n
for ex, -3, -2, -1, 0, 1, 1, 2
        ^ ^ ^ -- -> -3 - 2 + 2 = -3 < 0, move m pointer right
                 ^ ^ -- -> -3 - 1 + 2 = -2 < 0, move m pointer right
                ...
                       ^     ^  ---> -3 +1 +2 = 0 == 0, we found the match
                                                        move m -> right
                                                             n -> left
                          ^^    ---> break
            i    m           n
            ^    ^           ^  ---> move i to right and continue
"""

# pylint: skip-file


def search_triplet(arr):
    results = []
    n = len(arr)
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = len(arr) - 1
        # skip same element to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        while left < right:
            sum_ = arr[i] + arr[left] + arr[right]
            if sum_ == 0:
                results.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                right -= 1

    return results


print(search_triplet([-5, 2, -1, -1, -1, -1, -1, -2, 3]))
print(search_triplet([-2, 0, 0, 2, 2]))
