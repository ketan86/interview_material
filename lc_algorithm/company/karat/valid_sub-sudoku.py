"""
You are working on a logic game made up of a series of puzzles. The first type
of puzzle you settle on is "sub-Sudoku", a game where the player has to position
the numbers 1..N on an NxN matrix.

Your job is to write a function that, given an NxN matrix, returns true if every
row and column contains the numbers 1..N

The UI for the game does not do any validation on the numbers the player enters,
so the matrix can contain any signed integer.


Examples:

[[1, 3, 2],
[3, 1, 2],
[2, 3, 1]]

[[1, 2, 3],
[3, 1, 2],
[2, 3, 1]] -> True

[[1, 2, 3],
[1, 2, 3],
[1, 2, 3]] -> False

[[1, 1, 1],
[2, 2, 2],
[3, 3, 3]] -> False

[[1000, -1000, 6],
[ 2, 3, 1],
[ 3, 1, 2]] -> False

[[0]] -> False

[[3, 2, 3, 2],
[2, 3, 2, 3],
[3, 2, 3, 2],
[2, 3, 2, 3]] -> False

[[2, 3, 4],
[3, 4, 2],
[4, 2, 3]] -> False

[[-1,-2,-3],
[-2,-3,-1],
[-3,-1,-2]] -> False

[[1,1,1],
[1,1,2],
[1,2,3]] -> False
"""


def is_valid_sub_sudoku(grid):
    # find the length of the grid
    n = len(grid)
    # create a list of sets to store the unique values for each row and col
    row_set = [set() for _ in range(n)]
    col_set = [set() for _ in range(n)]

    # iterate over the grid
    for i in range(n):
        for j in range(n):
            num = grid[i][j]
            # if less than 1 or greater than n or already in row_set or col_set
            # return False
            if num < 1 or num > n or num in row_set[i] or num in col_set[j]:
                return False
            else:
                row_set[i].add(num)
                col_set[j].add(num)
    return True


test1 = [[1, 3, 2],
         [3, 1, 2],
         [2, 3, 1]]
test2 = [[1, 2, 3],
         [3, 1, 2],
         [2, 3, 1]]
print(is_valid_sub_sudoku(test1))
print(is_valid_sub_sudoku(test2))
