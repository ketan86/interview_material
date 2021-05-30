"""
Given a set of numbers that might contain duplicates, find all of its
distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3],
[1,3,3], [3,3,5], [1,5,3,3]
"""
# pylint: skip-file


def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            subset = list(subsets[i])
            subset.append(num)
            # if subset in subsets, ignore
            if subset not in subsets:
                subsets.append(subset)
    return subsets


def find_subsets_using_sorting(nums):
    # sort the list to get duplicates next to each other.
    nums.sort()

    subsets = []
    subsets.append([])
    # init variable to store the end index of the last subsets
    end_index_prev_num = 0
    for i in range(len(nums)):
        # always start looping over the existing set items with 0
        start_index = 0
        # if same element is found as previous, do not start with 0,
        # instead use the last stored end index + 1
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index_prev_num + 1
        # store end index as current subset length ( we have not added current
        # items and all other subsets)
        end_index_prev_num = len(subsets) - 1
        # add sets to subsets list
        for j in range(start_index, end_index_prev_num + 1):
            set_ = list(subsets[j])
            set_.append(nums[i])
            subsets.append(set_)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 2, 3, 3, 3])))

    print("Here is the list of subsets (using sorting): " +
          str(find_subsets_using_sorting([1, 3, 3])))
    print("Here is the list of subsets (using sorting): " +
          str(find_subsets_using_sorting([1, 2, 3, 3, 3])))


main()
