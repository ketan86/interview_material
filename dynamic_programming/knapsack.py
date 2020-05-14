def solve_knapsack(profits, weights, capacity):
    return find_profit(profits, weights, capacity, 0)


def find_profit(profits, weights, capacity, index, memo={}):
    # if there is not capacity left or index is out of bound, return 0
    if capacity < 0 or index >= len(profits):
        return 0

    if str(str(capacity) + ':' + str(index)) in memo:
        import pdb
        pdb.set_trace()
        return memo[str(str(capacity) + ':' + str(index))]

    # add current item in the profit or skip it.
    profit1 = 0
    # we can only add current item in the profile if it's weight is <= capacity
    if weights[index] <= capacity:
        # find the profile by adding the current item
        remaining_capacity = capacity - weights[index]
        profit1 = profits[index] + find_profit(
            profits, weights, remaining_capacity, index + 1)
    # find profit by skiping the current item
    profit2 = 0 + find_profit(profits, weights, capacity, index + 1)

    profit = max(profit1, profit2)

    memo[str(str(capacity) + ':' + str(index))] = profit

    return profit


print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
