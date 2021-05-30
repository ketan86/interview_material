"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be
verified from the merged
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""
# pylint: skip-file
import heapq


def find_Kth_smallest(matrix, k):
    """Runtime: 192 ms, faster than 61.32%

    Maintain kth smallest elements in the max_heap, top element will be
    the kth smallest.
    """
    max_heap = []

    # iterate over the matrix
    for row in matrix:
        for col in row:
            # put first k smallest elements
            if len(max_heap) < k:
                heapq.heappush(max_heap, -col)
            else:
                # if current element is smaller than top element, replace
                if -col > max_heap[0]:
                    heapq.heapreplace(max_heap, -col)

    return -max_heap[0]


def find_Kth_smallest_NOT_OPTIMAL(matrix, k):
    """Runtime: 216 ms, faster than 30.88%

    WHY WHY WHY ???? There is better solution using max_heap.
    NOTE: This solution uses 3 value tuple because heapq can not sort
    elements when first element of the tuple is same and second value is not
    comparable. Unless row/list defines compartor method (__lt__, __eq__,
    __gt__ etc..), heapq does not know how to sort values when first
    elements are same.

    """
    # use min_heap tp store the min value, index of that element in the list
    # and a pointer to the list
    min_heap = []
    # insert 0th element value, index and a list to min heap.
    for list_ in matrix:
        heapq.heappush(min_heap, (list_[0], 0, list_))

    # keep going until k -1 and min_heap.
    while k > 1 and min_heap:
        value, index, list_ = heapq.heappop(min_heap)
        # if next index of the list is less than the length, push the
        # element into the heap for processing.
        if index + 1 < len(list_):
            heapq.heappush(min_heap, (list_[index + 1], index + 1, list_))
        k -= 1

    # if min heap is empty, return -1
    if not min_heap:
        return -1

    # return the value of the kth smallest element.
    return heapq.heappop(min_heap)[0]


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 7, 8], [3, 5, 7], [1, 4]], 6)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()
