"""
Given base and n that are both 1 or more, compute recursively
(no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


powerN(3, 1) → 3
powerN(3, 2) → 9
powerN(3, 3) → 27
"""


def power_of_n(base, n):
    if n == 0:
        return 0
    if n == 1:
        return base

    return base * power_of_n(base, n - 1)


p = power_of_n(4, 3)
print(p)
