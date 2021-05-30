"""
https://leetcode.com/discuss/interview-question/1050247/Compass-first-round-via-Karat

The questions were followup questions.

1. For the given board where "0" is the position a player can move, -1 is the wall,
return all the possible moves from a given point. This was easy. O(1) solution
all test cases passed.

2. For the given board and an end point, return True if the
end can be reached from all other points in the board else False. O(MxN)
solution using DFS started from end and flagged the visited points and at the
end checked if there is any "0".

3. Given a board and start and end positions for
the player, write a function to return the shortest simple path of open spaces
from start to end that includes all the treasures, if any exist. If multiple
shortest paths exist, return any of them. A simple path is one that does not
revisit any location. This problem looks similar to -
https://leetcode.com/problems/squirrel-simulation/solution/

board3_1 = [
    [1,  0,  0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, -1,  0, 1, 0],
    [-1, 0,  0, 0, 0],
    [0,  1, -1, 0, 0],
    [0,  0,  0, 0, 0],
]

board3_2 = [
    [0,  1, -1],
    [0,  0,  0],
    [0,  0,  0],
]

treasure(board3_1, (5, 0), (0, 4)) -> None

treasure(board3_1, (5, 2), (2, 0)) ->
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3),
    (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
  Or
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3),
    (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

treasure(board3_1, (0, 0), (4, 1)) ->
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1)]
  Or
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]

treasure(board3_2, (2, 1), (1, 2)) ->
  [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (1, 2)]

board3_1 = [
    [1,  0,  0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, -1,  0, 1, 0],
    [-1,  0,  0, 0, 0],
    [0,  1, -1, 0, 0],
    [0,  0,  0, 0, 0],
]

board3_2 = [
    [0, 1, -1, ],
    [0, 0,  0, ],
    [0, 0,  0, ],
]

"""


def possible_ways(matrix, point):
    moves = []

    # check left
    left = point[1] - 1
    if left >= 0 and matrix[point[0]][left] == 0:
        moves.append((point[0], left))
    else:
        moves.append('X')

    # check right
    right = point[1] + 1
    if right < len(matrix[point[0]]) and matrix[point[0]][right] == 0:
        moves.append((point[0], right))
    else:
        moves.append('X')

    # check up
    up = point[0] - 1
    if up >= 0 and matrix[up][point[1]] == 0:
        moves.append((up, point[1]))
    else:
        moves.append('X')

    # check bottom
    bottom = point[0] + 1
    if bottom < len(matrix) and matrix[bottom][point[1]] == 0:
        moves.append((bottom, point[1]))
    else:
        moves.append('X')

    return moves


def end_can_be_reached(matrix, point):
    """Q: Can given point be reached from all other points ?"""

    dfs(matrix, point[0], point[1])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                return False

    return True


def dfs(matrix, row, col):

    if row < 0 or row > len(matrix) - 1 or \
        col < 0 or col > len(matrix[row]) - 1 or \
            matrix[row][col] == -1 or matrix[row][col] == 1:
        return

    matrix[row][col] = -1

    dfs(matrix, row+1, col)
    dfs(matrix, row-1, col)
    dfs(matrix, row, col+1)
    dfs(matrix, row, col-1)


def shortest_path(matrix, start, end):
    pass


matrix = [
    [1,  0,  0,      0, 0],
    [0, -1, -1,      0, 0],
    [0, -1,  0,      1, 0],
    [-1, 0,  0,      0, 0],
    [0,  1, -1,      0, 0],
    [0,  0,  0,      0, 0],
]

board3_2 = [
    [0,  1, -1],
    [0,  0,  0],
    [0,  0,  0],
]

print(possible_ways(matrix, (2, 4)))
print(end_can_be_reached(matrix, (2, 4)))
