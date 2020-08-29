"""
Conditional assigment using XOR
"""


def conditional_assignment(a, b):
    """
    XOR with self == 0
    """
    x = a
    # x = 10
    x = a ^ b ^ x
    # x = 20
    x = a ^ b ^ x
    # x = 10
    x = x ^ x
    # x = 0


conditional_assignment(10, 20)
