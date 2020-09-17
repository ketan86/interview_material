"""
Rotate bits by n in circular way.
"""

BIT_32_INTEGER = 32

"""
NOTE: Lets assume these numbers are 32 bit numbers.
Rotating number means moving some bits from right to left or left to right.
for ex, (9) 0000000000000000000000000000 1001, rotate by 2 clockwise,
0000000000000000000000000000 1001 -> 0100000000000000000000000000 0010

1001 : rotate right by 2
    1. isolate right most two bits. to isolate right most two bits, left shift
       int_size - k times.
       BIT_32_INTEGER - 2 = 30 times
        0000000000000000000000000000 1001 to
        0100000000000000000000000000 0000  <- 30 times left shifted

    2. right shift two bits.
        0000000000000000000000000000 1001 to
        0000000000000000000000000000 0010

    3. OR results
        0000000000000000000000000000 0010 OR
        0100000000000000000000000000 0000
        ---------------------------------
        0100000000000000000000000000 0010     (circular right shifted number by 2)

1001 : rotate left by 2
    1. isolate left most two bits. to isolate left most two bits, right shift
       int_size - k times.
       BIT_32_INTEGER - 2 = 30 times
        1100000000000000000000000000 1001
        0000000000000000000000000000 0011

    2. left shift two bits.
        0000000000000000000000000000 1001 to
        0000000000000000000000000010 0100

    3. OR results
        0000000000000000000000000010 0100 OR
        0000000000000000000000000000 0011
        ---------------------------------
        0000000000000000000000000010 0111     (circular left shifted number by 2)

"""


def rotate_clockwise(n, k):
    isolated_bits = n << (BIT_32_INTEGER - k)
    right_shifted_n = n >> k

    return isolated_bits | right_shifted_n


def rotate_anticlockwise(n, k):
    isolated_bits = n >> (BIT_32_INTEGER - k)
    right_shifted_n = n << k

    return isolated_bits | right_shifted_n


print(rotate_clockwise(3, 2))
print(rotate_clockwise(100, 7))
print(rotate_clockwise(4, 6))
print(rotate_clockwise(1, 7))

print(rotate_anticlockwise(3, 2))
print(rotate_anticlockwise(100, 7))
print(rotate_anticlockwise(4, 6))
print(rotate_anticlockwise(1, 7))
