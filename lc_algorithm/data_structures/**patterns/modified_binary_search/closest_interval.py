# // input: [[1, 3], [4, 7], [3, 8], [9, 10], [7, 9]]

# // output: [2, 4, 3, -1, 3]

# // For each interval [start_i, end_i], we want the index of the closest larger interval [start_j, end_j] to
# // such that end_i <= start_j
# //
# // Closest to the meaning, start_j being numerically closest to end_i
# //
# // Each start_i is unique
# //
# // -1 if no valid larger interval
# //
# // Input is not sorted
# //
# // Intervals are always increasing


"""
[[1, 3], [4, 7], [3, 8], [9, 10], [7, 9]]

[1, 3] [3, 8][4, 7][7, 9][9, 10]
                    ^
  1 -> [1, 3],
  3 -> [3, 8], 
  4 -> [4, 7], 
  7 -> [7, 9],
  9 -> [9, 10],index  


  [1, 9],
  [3, 10], 
  [4, 11], 
  [7, 12],
  [9, 13],index  

"""


def find_valid_larger_interval(intervals):
    if not intervals:
        return []

    result = [-1] * len(intervals)

    interval_index_map = {}
    for index, interval in enumerate(intervals):
        interval_index_map[tuple(interval)] = index

    intervals.sort()

    for index, interval in enumerate(intervals):
        end_time = interval[1]
        output = binary_search(intervals, index, len(intervals)-1, end_time)
        if output == -1:
            result[interval_index_map[tuple(interval)]] = -1
        else:
            result[interval_index_map[tuple(
                interval)]] = interval_index_map[output]

    return result


def binary_search(intervals, start_index, end_index, end_time):
    index = - 1
    start_time = float('inf')
    # [3, 8][4, 7][7, 9][9, 10]
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if intervals[mid][0] < end_time:
            start_index = mid + 1
        elif intervals[mid][0] > end_time:
            if intervals[mid][0] < start_time:
                start_time = intervals[mid][0]
                index = tuple(intervals[mid])
            end_index = mid - 1
        else:
            return tuple(intervals[mid])

    return index


print(find_valid_larger_interval([[1, 3], [4, 7], [3, 8], [9, 10], [7, 9]]))
