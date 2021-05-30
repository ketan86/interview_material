"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into
one big rope with minimum cost. The cost of connecting two ropes is equal to
the sum of their lengths.

Example 1:

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the
total cost is 33 (4+9+20)

Example 2:

Input: [3, 4, 5, 6]
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is
36 (7+11+18)

Example 3:

Input: [1, 3, 11, 5, 2]
Output: 42
Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22).
Total cost is 42 (3+6+11+22)
"""
# pylint: skip-file
import heapq


def minimum_cost_to_connect_ropes(rope_lengths):
    # define min_heap list
    min_heap = []
    # total cost for connection
    total_cost = 0
    # push all lengths to min heap
    for rope_length in rope_lengths:
        heapq.heappush(min_heap, rope_length)

    # read first two values and save sum to total sum and push sum to heap
    # until last two values are left.
    while min_heap:
        sum_ = heapq.heappop(min_heap) + heapq.heappop(min_heap)
        total_cost += sum_
        # push sum of the top two values into heap for further calculation
        if min_heap:
            heapq.heappush(min_heap, sum_)

    # return total cost
    return total_cost


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
