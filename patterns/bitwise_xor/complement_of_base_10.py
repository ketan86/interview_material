"""
Every non-negative integer N has a binary representation, for example,
8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we
get when we change every 1 to a 0 and every 0 to a 1. For example, the binary
complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary
representation as a base-10 integer.

Example 1:

Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary,
which is 7 in base-10.
Example 2:

Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary,
which is 5 in base-10.
"""

# pylint: skip-file


def calculate_bitwise_complement(n):
    # count number of bits. 
    # right bitwise shift until reaches 0. 
    # for ex, 8, 8 >> 1 = 4, 4 >>1 = 2, 2 >>1 = 1,  1 >>1 = 0
    # (total 4 operations)
    bits = 0
    num = n
    while num > 0:
        bits += 1
        num >>= 1

    # create all bits set to 1.
    # if you XOR number with all 1's, you get the complement.
    # for ex, 8 contains 4 bits, 2 ^ 4 = 16 (10000)
    # to reduce to 4 digits all set to 1, 16 -1 = 15 (1111)
    all_bits_set = pow(2, bits) - 1

    return n ^ all_bits_set


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
