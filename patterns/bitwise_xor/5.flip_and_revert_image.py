"""
Given a binary matrix representing an image, we want to flip the image
horizontally, then invert it.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced
by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

Example 1:

Input: [
  [1,0,1],
  [1,1,1],
  [0,1,1]
]
Output:

reverse:
[
  [1,0,1],
  [1,1,1],
  [1,1,0]

]
invert:
[
  [0,1,0],
  [0,0,0],
  [0,0,1]
]
Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert
the image: [[0,1,0],[0,0,0],[0,0,1]]

Example 2:

Input: [
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1],
  [1,0,1,0]
]
Output: [
  [1,1,0,0],
  [0,1,1,0],
  [0,0,0,1],
  [1,0,1,0]
]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
"""
# pylint: skip-file

# Using the XOR property, we can XOR the bits with 1 and swap.


def flip_and_invert_image(matrix):
    for row in matrix:
        i = 0
        j = len(row) - 1
        while i <= j:
            # XOR(0 ^ 1 = 1, 1 ^ 1 = 0) and Swap
            row[i], row[j] = row[j] ^ 1, row[i] ^ 1
            i += 1
            j -= 1
    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
