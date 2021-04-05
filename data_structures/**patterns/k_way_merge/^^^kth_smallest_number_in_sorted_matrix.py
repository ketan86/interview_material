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
    """
    NOTE: This solution uses 3 value tuple because heapq can not sort
    elements when first element of the tuple is same and second value is not
    comparable. Unless row/list defines compartor method (__lt__, __eq__,
    __gt__ etc..), heapq does not know how to sort values when first
    elements are same.
    """
    # use min_heap tp store the value, index of that element in the row
    # and a pointer to the row.
    min_heap = []
    # insert 0th element value, index and a row to min heap.
    for row in matrix:
        heapq.heappush(min_heap, (row[0], 0, row))

    # keep going until k -1 and min_heap.
    while k > 1 and min_heap:
        value, index, row = heapq.heappop(min_heap)
        # if next index of the list is less than the length, push the
        # element into the heap for processing.
        if index + 1 < len(row):
            heapq.heappush(min_heap, (row[index + 1], index + 1, row))
        k -= 1

    # if min heap is empty, return -1
    if not min_heap:
        return -1

    # return the value of the kth smallest element.
    return heapq.heappop(min_heap)[0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
