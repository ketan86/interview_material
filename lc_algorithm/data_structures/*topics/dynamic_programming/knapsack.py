"""
0/1 Knapsack:

Capacity = 7
Items   :  1   2   3   4
Weight :  1   3   4   5
Profit   :  1   4    5   7

Find maximum profit

Choice Diagram:
                   w1
           /                 \
w1 <= capacity    w1 > capacity
      /  \                       |
  yes  no                  no


def find_max_profit(weights, profits, index, capacity):
        # base condition
        # choice diagram


Find base condition:

* think of the smallest valid input 
    * index can be 0
    * capacity can be 0
* profit will be 0 if no items or capacity is 0, max profit will be 0

Choice Diagram:  recursion should reduce it’s size

* if weight is less than equal to capacity
    * max(
        current + find_max_profit(
            weights, profits, index + 1, capacity -  current[weight]),
        find_max_profit(weights, profits, index + 1, capacity)
    )
* if weight is greater than capacity
    *  find_max_profit(weights, profits, index + 1, capacity)
"""

def find_max_profit(weights, profits, capacity):
    return max_profit(weights, profits, 0, capacity)

def max_profit(weights, profits, index, capacity):
    # if capacity is 0 or no item, max profit is 0
    if capacity == 0 or index == len(weights):
        return 0

    # if weight of the item is equal or less than the capacity
    if weights[index] <= capacity:
        # we have two choices, include current item or not. max of both
        return max(
            # include current item
            profits[index] + max_profit(
                weights, profits, index + 1, capacity - weights[index]),
            # do not include current item
            max_profit(weights, profits, index + 1, capacity)
        )
    else:
        # do not include current item
        return max_profit(weights, profits, index + 1, capacity)


def find_max_profit_memo(weights, profits, capacity):
    return max_profit_memo(weights, profits, 0, capacity, memo={})

def max_profit_memo(weights, profits, index, capacity, memo):
    """Memoize data that is variable. In this case, capacity and index
    is decreasing so we can use that to store the profit at given values.

                                   i=0, c=7
                    /w[i] <= c                 w[i] > c \
    max(i+1, c-p[i],  i+1, c)                         i+1,c
          /w[i] <= c     \w[i] > c
        ..........

    """
    # if capacity is 0 or no item, max profit is 0
    if capacity == 0 or index == len(weights):
        return 0

    if f'{index}:{capacity}' in memo:
        return memo[f'{index}:{capacity}']

    # if weight of the item is equal or less than the capacity
    if weights[index] <= capacity:
        # we have two choices, include current item or not. max of both
        profit = max(
            # include current item
            profits[index] + max_profit(
                weights, profits, index + 1, capacity - weights[index]),
            # do not include current item
            max_profit(weights, profits, index + 1, capacity)
        )
        memo[f'{index}:{capacity}'] = profit
        return profit
    else:
        # do not include current item
        profit = max_profit(weights, profits, index + 1, capacity)
        memo[f'{index}:{capacity}'] = profit
        return profit



def find_max_profit_top_down(weights, profits, capacity):
    """
    In bottom up (recursion), we start with a bigger problem and break down
    it to smaller problem whereas in top down approach, we start solving the
    smallest problem and build solution to bigger problem using smaller
    solutions.

    capacity      0 1 2 3 4 5
                  -----------
    index  []  0 |0 0 0 0 0 0
           0   1 |0 0 <--------- *max(curr profit + previous profit when capacity
           1   2 |0                  reduces to capacity - current weight,
           2   3 |0                  same profit as previous
                                 )
                                 if current weight is <= capacity
                                 else,
                                 * same profit as previous

    weights = [2,4,3]
    profits = [1,6,9]
    capacity = 5
    """
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights) + 1):
        for c in range(capacity + 1):
            # smaller solution when no items or capacity
            if i == 0 or c == 0:
                dp[i][c] = 0
            # if weight is <= capacity, we can find the profit
            elif weights[i-1] <= c:
                # include current profit in previous profit found so far 
                # or exclude and go with previous profit
                dp[i][c] = max(
                    profits[i-1] + dp[i-1][c - weights[i - 1]],
                    dp[i-1][c]
                )
            else:
                # if weight is > capacity, exclude current profit and use
                # profit calculated so far to find the current profit.
                dp[i][c] = dp[i-1][c]

    return dp[len(weights)][capacity]

print(find_max_profit([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(find_max_profit([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(find_max_profit_memo([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(find_max_profit_memo([1, 6, 10, 16], [1, 2, 3, 5], 6))

print(find_max_profit_top_down([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(find_max_profit_top_down([1, 6, 10, 16], [1, 2, 3, 5], 6))
