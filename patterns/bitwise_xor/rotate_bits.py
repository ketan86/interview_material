"""
Rotate bits by n in circular way.
"""

def rotate_clockwise(n, k):
    pass

"""
NOTE: Lets assume these numbers are 32 bit numbers.
Rotating number means moving some bits from right to left or left to right.
for ex, (9) 0000000000000000000000000000 1001, rotate by 2 clockwise,
0000000000000000000000000000 1001 -> 0000000000000000000000000000 0110

1. 0000000000000000000000000000 1001
    -> right shift >> 2 times 0000000000000000000000000000 0010
2. 0000000000000000000000000000 1001
    -> left shift << 2 times  0000000000000000000000000010 0100
3. 0000000000000000000000000000 0010 (2)
   0000000000000000000000000010 0100 (36)   OR
   --------------------------------
   0000000000000000000000000010 0110
"""

print(rotate_clockwise(3, 2))
print(rotate_clockwise(100, 7))
print(rotate_clockwise(4, 6))
print(rotate_clockwise(1, 7))