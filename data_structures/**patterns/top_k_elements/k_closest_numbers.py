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
import heapq


def find_closest_elements(arr, k, x):
    min_heap = []
    for i in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, i)
        else:
            # if abs(min_element - x) is greater than abs(i - x), replace the
            # heap element
            curr_diff = abs(x - min_heap[0])
            new_diff = abs(x - i)
            if new_diff < curr_diff:
                heapq.heapreplace(min_heap, i)
    return sorted(min_heap)

# since array is sorted, reduce the search area finding the place where
# we could search both sides for k elements.


def find_closest_elements_efficient(arr, k, x):
    min_heap = []
    index = _binary_search(arr, x)

    # low and high together on each side can not be more than k elements.
    # so we consider the worse case where all elements are in left or in
    # right. so consider total of k * 2 elements.
    low = index - k
    high = index + k
    low = max(low, 0)
    high = min(len(arr) - 1, high)

    # go from low to hight and put all elementes in heap sorted by their diff
    # from origin x.
    for i in range(low, high + 1):
        heapq.heappush(min_heap, (abs(arr[i] - x), arr[i]))

    # pop k elements from the heap and return the sorted results.
    result = []
    for _ in range(k):
        result.append(heapq.heappop(min_heap)[1])

    return sorted(result)


def find_closest_elements_efficient_2(arr, k, x):
    min_heap = []
    index = _binary_search(arr, x)
    # insert the first closest element in heap
    heapq.heappush(min_heap, arr[index])
    # define two pointers
    i = index - 1
    j = index + 1

    count = k - 1
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


def _binary_search(arr, x):
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if x < arr[mid]:
            end_index = mid - 1
        elif x > arr[mid]:
            start_index = mid + 1
        else:
            return mid

    return end_index


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

    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: (BinarySearch-2) " +
          str(find_closest_elements_efficient_2(
              [1, 2, 2, 2, 2, 2, 2, 3], 3, 10)))


main()
