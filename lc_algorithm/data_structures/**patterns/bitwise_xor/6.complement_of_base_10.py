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
    """
    The goal here is find the same length number with all bits set that can be
    XORed with the current number to flip the bits.

    Steps:
        1. count number of bits in the original number.
            count = 8(1000) -> total bits 4
        2. left_shifted = left shift 1 to that many bits
            left_shifted = 1 << count(4) -> 16(10000)
        3. new = subtract 1 from the left_shifted
            new = left_shifted - 1 -> 15(1111)
        4. XOR new and original number
            result = new(15) ^ original(8) -> 0111(7)

    1 << (no of bits) - 1 -> gives all bits set
    for ex, 8(1000) = 1 << 4 (16)(10000) - 1 = 15(1111) -> all bits are set
            25 = 1 << 5 (32) - 1 = 31 -> all bits are set
    """
    # count number of bits.
    # right bitwise shift until reaches 0.
    # for ex, 8, 8 >> 1 = 4, 4 >>1 = 2, 2 >>1 = 1,  1 >>1 = 0
    # (total 4 operations)
    bits = 0
    num = n

    while num > 0:
        bits += 1
        num >>= 1

    # generate a number with all bits set to 1.
    # if you XOR number with all 1's, you get the complement.
    # for ex, 8 contains 4 bits, 2 ^ 4 = 16 (10000)
    # to reduce to 4 digits all set to 1, 16 -1 = 15 (1111)
    all_bits_set = (1 << bits) - 1

    # XOR with 1 gives the complement.
    return n ^ all_bits_set


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
