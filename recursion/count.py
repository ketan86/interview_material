"""

Given a non-negative int n, return the count of the occurrences of 7 
as a digit, so for example 717 yields 2. (no loops). Note that mod (%) 
by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 
removes the rightmost digit (126 / 10 is 12).
"""


def count(n, digit):
    if n // 10 == 0:
        if n == digit:
            return 1
        return 0

    remainder = n % 10

    if remainder == digit:
        return count(n // 10, digit) + 1

    return count(n // 10, digit)


c = count(7777, 7)
print(c)


"""
Given a non-negative int n, compute recursively (no loops) the count
of the occurrences of 8 as a digit, except that an 8 with another 8
immediately to its left counts double, so 8818 yields 4. Note that
mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while
divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


count8(8) → 1
count8(818) → 2
count8(8818) → 4
"""


def count(n, digit, found=False):
    if n // 10 == 0:
        if n == digit and found:
            return 2
        elif n == digit and not found:
            return 1
        return 0

    remainder = n % 10

    if remainder == digit:
        if found:
            return count(n // 10, digit, True) + 2
        else:
            return count(n // 10, digit, True) + 1

    return count(n // 10, digit, False)


c = count(7177, 7)
print(c)
