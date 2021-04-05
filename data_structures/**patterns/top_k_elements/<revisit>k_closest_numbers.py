"""
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’
closest numbers to ‘X’ in the array. Return the numbers in the sorted
order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
"""

# pylint: skip-file
from collections import deque
import heapq


# O(n)
def find_closest_elements(arr, k, x):
    # maintain min heap to store
    min_heap = []
    for i in arr:
        # until min heap contains k elements, add number in the min_heap
        if len(min_heap) < k:
            heapq.heappush(min_heap, i)
        else:
            # if abs(min_element - x) is greater than abs(i - x), replace the
            # heap element

            # find the distance of the number and min_heap top element from x
            curr_diff = abs(x - min_heap[0])
            new_diff = abs(x - i)

            # if new diff is less than the top element diff, replace min heap
            # with current element.
            if new_diff < curr_diff:
                heapq.heapreplace(min_heap, i)

    result = []
    for _ in range(k):
        result.append(heapq.heappop(min_heap))

    return result

# O(logn + k)
# since array is sorted, reduce the search area finding the place where
# we could search both sides for k elements.


def find_closest_elements_efficient(arr, k, x):
    """Using binary search, find the element (if present) or at lease the
    closest number. After that, there is no guaranty on which side k elements
    fall. All k elements could be on left or right or divided on both side so
    consider k elements on left and k elements on right to cover all cases.
    Total elements processed would be k*2.


    NOTE: since we are considering the left element when target is not found,
    we can reduce the k by 1 on left for low index since it will be either be
    included or if not, current element is already one of the closest element.

    """
    min_heap = []
    # find the target using the binary search
    index = _binary_search(arr, x)

    # low and high together on each side can not be more than k elements.
    # so we consider the worse case where all elements are in left or in
    # right. so consider total of k * 2 elements.
    low = max(index - k, 0)
    high = min(len(arr) - 1, index + k)

    # go from low to hight and put all elements in heap sorted by their diff
    # from origin x.
    # min_heap -> (diff, num)
    for i in range(low, high + 1):
        heapq.heappush(min_heap, (abs(arr[i] - x), arr[i]))

    # pop k elements from the heap and return the results.
    result = []
    for _ in range(k):
        result.append(heapq.heappop(min_heap)[1])

    # NOTE: This is not efficient as sorting of elements is required.
    return sorted(result)


def _binary_search(arr, target):
    # This binary search finds the target or left element of the target if
    # target is not present.
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if target < arr[mid]:
            end_index = mid - 1
        elif target > arr[mid]:
            start_index = mid + 1
        else:
            return mid

    return end_index


def find_closest_elements_efficient_2(arr, k, x):
    """"Using binary search, find the closest element (if present) or at lease
    the closest number. Define two pointers and move based on the diff. When
    all k elements are found, return the subarray starting from i to j.
    """
    if k == 0:
        return []

    # if target is <= first element, return all elements from 0 to kth index
    if x <= arr[0]:
        return arr[:k]

    # if target is >= last element, return all elements from last kth index
    # to end.
    if x >= arr[-1]:
        return arr[len(arr)-k:]

    # find the target using the binary search.
    index = _binary_search_closest_NOT_WORKING(arr, x)

    # define two pointers
    i = j = index

    # save k into a count
    count = k

    # move i and j based on their diff to target
    while i >= 0 and j < len(arr) and count > 0:
        left_diff = abs(arr[i] - x)
        right_diff = abs(arr[j] - x)
        if left_diff < right_diff:
            i -= 1
        else:
            j += 1
        count -= 1

    # if count is not 0 and i not 0, move i and count
    while i >= 0 and count > 0:
        i -= 1
        count -= 1

    # if count is not 0 and j not 0, move j and count
    while j < len(arr) and count > 0:
        j += 1
        count -= 1

    # because i and j are already decremented/incremented when count is 0,
    # exclude i and j.
    return arr[i:j]


def _binary_search_closest_NOT_WORKING(arr, target):
    # This binary search finds the target or left element of the target if
    # target is not present.
    start_index = 0
    end_index = len(arr) - 1
    prev_diff = float('inf')
    closest = -1
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        current_diff = abs(arr[mid] - target)
        new_prev_diff = min(prev_diff, current_diff)
        if current_diff == 0:
            return mid
        if current_diff > new_prev_diff:
            end_index = mid - 1
        else:
            start_index = mid + 1
            closest = mid
            prev_diff = new_prev_diff

    return closest


def find_closest_elements_efficient_2_FAIL(arr, k, x):
    # THIS SOLUTION FAILS BECAUSE WE ARE NOT FINDING THE CLOSEST ELEMENT
    # OF THE TARGET DURING THE BINARY SEARCH. THE STARTING INDEX DURING
    # THE EXPANSION MATTERS,
    # FOR EX, [1, 1, 1, 10, 10, 10], K=1 TARGET=9
    # If we start with index 2 (value 1), we will only expand towards left
    # and return [1] instead of [10]
    """"Using binary search, find the element (if present) or at lease the
    closest number. Define two pointers and move based on the diff. When
    all k elements are found, return the subarray starting from i to j.
    """
    if k == 0:
        return []

    # if target is <= first element, return all elements from 0 to kth index
    if x <= arr[0]:
        return arr[:k]

    # if target is >= last element, return all elements from last kth index
    # to end.
    if x >= arr[-1]:
        return arr[len(arr)-k:]

    min_heap = []

    # do simple binary search but use min_heap to hold 1 or 2 extra elements
    # and during pop, only use k elements.
    # NOTE: Need to find the closest element of target x.
    index = _binary_search(arr, x)
    # insert the first closest element in heap
    heapq.heappush(min_heap, arr[index])
    # define two pointers
    i = index - 1
    j = index + 1

    count = k
    while i >= 0 and j < len(arr):
        if count == 0:
            break
        left_diff = abs(arr[i] - x)
        right_diff = abs(arr[j] - x)
        if left_diff < right_diff:
            heapq.heappush(min_heap, arr[i])
            i -= 1
        else:
            heapq.heappush(min_heap, arr[j])
            j += 1
        count -= 1

    while i >= 0 and count > 0:
        heapq.heappush(min_heap, arr[i])
        i -= 1
        count -= 1

    while j < len(arr) and count > 0:
        heapq.heappush(min_heap, arr[j])
        j += 1
        count -= 1

    result = []
    for i in range(k):
        result.append(heapq.heappop(min_heap))

    return result


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

    print("'K' closest numbers to 'X' are: (BinarySearch) " +
          str(find_closest_elements_efficient([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: (BinarySearch) " +
          str(find_closest_elements_efficient([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: (BinarySearch) " +
          str(find_closest_elements_efficient([2, 4, 5, 6, 9], 3, 10)))
    print("'K' closest numbers to 'X' are: (BinarySearch) " +
          str(find_closest_elements_efficient(
              [1, 1, 1, 10, 10, 10], 3, 9)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2([2, 4, 5, 6, 9], 3, 10)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2(
              [1, 2, 2, 2, 2, 2, 2, 3], 3, 10)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2(
              [1, 2, 3, 4, 5], 4, 3)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2(
              [1, 1, 1, 10, 10, 10], 1, 9)))


main()
