"""
We'll say that a "pair" in a string is two instances of a
char separated by a char. So "AxA" the A's make a pair. Pair's
can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x.
Recursively compute the number of pairs in the given string.


countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
"""


def count_pairs(s):

    if len(s) == 1 or len(s) == 2:
        return 0
    if len(s) == 3:
        if s[0] == s[2]:
            return 1
        return 0

    return count_pairs(s[:3]) + count_pairs(s[1:])


n = count_pairs('axbx')
print(n)
