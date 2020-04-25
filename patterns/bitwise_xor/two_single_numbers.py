"""
Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except
two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]


XOR TABLE:
    0 0 -> 0
    0 1 -> 1
    1 0 -> 1
    1 1 -> 0
"""
# pylint: skip-file


def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # After XORing, we get a number that is XOR of two single numbers.
    # for ex, [1, 4, 2, 1, 3, 5, 6, 2, 3, 5],
    # after XOR, 4 ^ 6 = 2
    #       0 1 0 0
    #       0 1 1 0
    #       -------
    #       0 0 1 0   <- after all other duplicates are cancelled out,
    #                    XOR or 4 and 6 would be resulted in a number
    #                    where first set bit (1) for right, would be
    #                    because of XOR or 0 and 1. If we separate 4 and 6
    #                    into two groups, where one group contains all
    #                    numbers where second bit is 0 and other group with
    #                    second bit to 1, we can then process those two
    #                    groups separately to find those two numbers.

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    # Bit wise left shifting moves 1 from right to left one at a time.
    # a = 1, a <<=1 = 2, a <<=1 = 4, 8 , 16 , 32 and so on.
    # keep shifting 1 till n1xn2 AND rightmost_set_bit value is not zero.
    # for ex,
    # 4 ^ 6 = 2,
    # 10 & 01 -> 00, left shift
    # 10 & 10 -> 10, found digit
    # so rightmost_set_bit will be set to right value.

    num1, num2 = 0, 0
    for num in nums:
        # muliply number with rightmost_set_bit and if it is not 0, XOR with
        # num1 else num2
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
