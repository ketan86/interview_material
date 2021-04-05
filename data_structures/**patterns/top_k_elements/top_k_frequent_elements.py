"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring
numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""
# pylint: skip-file
from collections import defaultdict
import heapq


def find_k_frequent_numbers(nums, k):
    # use min heap
    min_heap = []
    # freq map to store the number and freq of each number
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # iterate over the freq map
    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            if freq > min_heap[0][0]:
                heapq.heapreplace(min_heap, (freq, num))

    return [num for _, num in min_heap]


def _print(result):
    result_copy = list(result)
    while result_copy:
        print(heapq.heappop(result_copy))


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 2, 5, 2, 12, 2, 12], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
