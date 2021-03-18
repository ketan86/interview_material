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


def search_triplet(nums):
    """
    Key of this problem is **sorting** and skipping **duplicate** elements.
    """
    results = []
    if not nums:
        return results
    nums.sort()

    # go till 3rd last element
    for i in range(len(nums) - 2):
        # if i value is greater than 0, sum will never be 0.
        # for ex, [1,3,4,8..]
        if nums[i] > 0:
            break

        # if we find the current element same as prev, skip it to eliminate
        # duplicates.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # two pointers to find the diff
        x = j = i + 1
        y = k = len(nums) - 1

        # only till j < k and NOT j <=k because we need two elements
        while j < k:
            # if prev value of the j or k is same, skip j or k.
            # NOTE: j > x and y < k (next condition) is to prevent
            # j from matching the i and k from going out of
            # bound in the first iteration.
            if j > x and nums[j] == nums[j - 1]:
                j += 1
                continue

            if y > k and nums[k] == nums[k + 1]:
                k -= 1
                continue

            # sum of all the elements
            sum_ = nums[i] + nums[j] + nums[k]
            # if sum is 0, record the results and increment j and k
            if sum_ == 0:
                results.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            # if sum is less than the target(0), increment j to reach
            # close to target. else decrement k
            elif sum_ < 0:
                j += 1
            else:
                k -= 1

    return results


print(search_triplet([-5, 2, -1, -1, -1, -1, -1, -2, 3]))
print(search_triplet([-2, 0, 0, 2, 2]))
