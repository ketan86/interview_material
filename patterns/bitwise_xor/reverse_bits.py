# pylint: skip-file
def reverse_bit(num):
    # right shift num, AND with 1 and OR with the left shifted result.
    result = 0
    while num:
        result = (result << 1) | (num & 1)
        num >>= 1
    return result


"""
Steps :
    strip off the last bit, & with 1 and add it to results.
    0b010,     0 & 1 = 0 <- result 0b0
    0b01       1 & 1 = 1, left shift result 0b0 and add 1 to it. 0b01
    ...
"""

"""
num = 0b11100110, result = 0
while:
    result = 0b0 << 1 = 0b0 + 0b11100110 & 0b1 = 0b0, result = 0b0
    0b11100110 >> 1 = 0b1110011

    result = 0b0 << 1 = 0b0 + 0b1110011 & 0b1 = 0b1, result = 0b1
    0b1110011 >> 1 = 0b111001

    result = 0b01 << 1 = 0b010 + 0b111001 & 1 = 0b1, result = 0b011
    0b111001 >> 1 = 0b11100

    result = 0b011 << 1 = 0b0110 + 0b11100 & 1 = 0b0, result = 0b0110
    0b11100 >> 1 = 0b1110

    ...
"""

# We don't really need to convert the integer into binary, since integers
# are actually represented binary in Python.
# The reversing idea is like doing the in-space reversing of integers.


def reverse_int(x):
    result = 0
    pos_x = abs(x)
    while pos_x:
        result = result * 10 + pos_x % 10
        pos_x //= 10
    return result if x >= 0 else (-1) * result


"""
num = -123, result = 0
pos = 123
while:
    result = 0 * 10 + 3 % 10 = 3
    pos = 123//10 = 12

    result = 3 * 10 + 12 % 10 = 32
    pos = 12//10 = 1

    result = 32 * 10 + 1 % 10 = 321
    pos = 1//10 = 0

return 321


"""
# For each loop, the original number is dropping the right-most bit
# (in binary). We get that right-most bit and multiply 2 (<<1) in the
# next loop when the new bit is added.

print(reverse_bit(5))
print(reverse_int(125))
print(reverse_bit(34))
print(reverse_int(34))
