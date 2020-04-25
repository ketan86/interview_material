"""
Given an N * N matrix where each row and column is sorted in ascending
order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8],
    [3, 7, 10],
    [5, 8, 11]
  ]
K=5

Output: 7
Explanation: The 5th smallest number in the matrix is 7.
"""
# pylint: skip-file
import heapq


def find_Kth_smallest(matrix, k):
    min_heap = []
    for row in matrix:
        heapq.heappush(min_heap, (row[0], 0, row))

    while k > 1 and min_heap:
        value, index, row = heapq.heappop(min_heap)
        if index + 1 < len(row):
            heapq.heappush(min_heap, (row[index + 1], index + 1, row))
        k -= 1
    return heapq.heappop(min_heap)[0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
