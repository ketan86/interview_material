"""
This was for an mid-level role at Roblox.

Find the top left and bottom right coordinates of a rectangle of 0's within a
matrix of 1's. It's essentially a modified version of the finding the number
of island problem where you only need to dfs to the right and down.
Ex.
[[ 1, 1, 1, 1],
[ 1, 0, 0, 1],
[ 1, 0, 0, 1],
[ 1, 1, 1, 1]]
Expected output: [[1,1], [2,2]]

Follow up question: Expand it so it works for any number of rectangles.
Main part of this problem is updating how results are stored and tracking
what's been seen.
Ex.
[[0, 1, 1, 1],
[1, 0, 0, 1],
[1, 0, 0, 1],
[1, 1, 1, 1]]
Expected output: [ [[0,0],[0,0]], [[1,1], [2,2]] ]

https://leetcode.com/problems/number-of-islands
"""


def find_zeros(matrix):
    # store results
    result = []
    # iterate over the matrix. find rectangle when 0 is found.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                # find the end indexes
                end = dfs(matrix, i, j)
                # append start and end. dfs increases index by 1 so decrement
                # index by 1.
                result.append([[i, j], [end[0] - 1, end[1] - 1]])
    return result


def dfs(matrix, row, col):
    # if row and col is out of bound or value is not zero. return [row and col]
    if row >= len(matrix) or col >= len(matrix[row]) or matrix[row][col] != 0:
        return [row, col]

    # mark visited items to 1
    matrix[row][col] = 1

    # traverse down and right to find the end.
    new_row, _ = dfs(matrix, row + 1, col)
    _, new_col = dfs(matrix, row, col + 1)

    # return row of the dfs that was traversed
    return [new_row, new_col]


matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

print(find_zeros(matrix))


matrix = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]
print(find_zeros(matrix))


m0 = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]]
print(find_zeros(m0))

r0 = [[[1, 1], [2, 2]]]

m1 = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]]
print(find_zeros(m1))

r1 = [[[0, 0], [0, 0]], [[1, 1], [2, 3]]]

m2 = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 0]]
print(find_zeros(m2))

r2 = [[[0, 0], [0, 0]], [[1, 1], [2, 2]], [[3, 3], [3, 3]]]

m3 = [
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0],
]
print(find_zeros(m3))

r3 = [
    [[0, 0], [0, 0]],
    [[2, 0], [2, 0]],
    [[2, 3], [3, 5]],
    [[3, 1], [5, 1]],
    [[5, 3], [6, 4]],
    [[7, 6], [7, 6]],
]
