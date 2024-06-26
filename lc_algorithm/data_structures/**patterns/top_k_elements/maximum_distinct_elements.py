"""
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers
from the array such that we are left with maximum distinct numbers.

Example 1:

Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct
numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be
left with three 
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it
occurred twice.
Example 2:

Input: [3, 5, 12, 11, 12], and K=3
Output: 2
Explanation: We can remove one occurrence of 12, after which all numbers
will become distinct. Then 
we can delete any two numbers which will leave us 2 distinct numbers in
the result.
Example 3:

Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
Output: 3
Explanation: We can remove one occurrence of '4' to get three distinct numbers.

"""
# pylint: skip-file
from collections import defaultdict
import heapq


def find_maximum_distinct_elements(nums, k):

    # define freq map
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # count distinct numbers and put non-distinct into min_heap (freq sorted)
    min_heap = []
    distinct = 0

    # make min heap of only non-distinct numbers
    for num, freq in freq_map.items():
        if freq == 1:
            distinct += 1
        else:
            heapq.heappush(min_heap, (freq, num))

    # until k reduce to 0, process min heap elements and remove freq -1
    # if k is till >= 0, consider that distinct
    while k > 0 and min_heap:
        freq, num = heapq.heappop(min_heap)
        k -= freq - 1
        if k >= 0:
            distinct += 1

    # if k is greater than 0, remove that many distinct numbers
    if k > 0:
        distinct -= k

    return distinct


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
