"""
Swap two numbers without temp variable.
"""


def swap(a, b):
    """
    XOR property of bits, make this possible.

    a = 1 b = 0

    a = a ^ b = 1 ^ 0 = 1
    b = a ^ b = 1 ^ 0 = 1
    a = a ^ b = 1 ^ 1 = 0

    a = 0 and b = 1
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


print(swap(10, 20))
