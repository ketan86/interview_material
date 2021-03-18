"""
We have triangle made of blocks. The topmost row has 1 block, the next row 
down has 2 blocks, the next row has 3 blocks, and so on. Compute 
recursively (no loops or multiplication) the total number of 
blocks in such a triangle with the given number of rows.
"""


def triangle(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return triangle(n - 1) + 2


t = triangle(5)
print(t)
