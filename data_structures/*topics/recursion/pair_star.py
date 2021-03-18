"""
Given a string, compute recursively a new string where identical
chars that are adjacent in the original string are separated from
each other by a "*".


pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
"""


def insert_btw_pair(s, char):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s[0] + char + s[1]
        return s

    left = insert_btw_pair(s[:2], char)
    right = insert_btw_pair(s[2:], char)

    if left[-1] == right[0]:
        return left + char + right
    return left + right


s = insert_btw_pair('abccdccd', '*')
print(s)
