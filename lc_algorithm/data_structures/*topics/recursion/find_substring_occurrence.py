"""

Given a string, compute recursively (no loops) the number of 
times lowercase "hi" appears in the string.


countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1
"""


def find_substring_occurrence(s, sub):
    if len(s) == 1:
        return 0

    if len(s) == 2:
        if s == sub:
            return 1
        return 0

    return find_substring_occurrence(
        s[:2], sub) + find_substring_occurrence(s[2:], sub)


o = find_substring_occurrence('abhihicd', 'hi')
print(o)
