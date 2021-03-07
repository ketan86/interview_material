"""Using XOR property, we can find odd occuring number in the list
of numbers"""


def odd_occuring_number(nums):
    """XOR cancels out the number that are in pair.

    property : x ^ x -> 0
    """
    result = 0
    for num in nums:
        result ^= num
    return result


print(odd_occuring_number([12, 12, 14, 90, 90, 14, 14]))
