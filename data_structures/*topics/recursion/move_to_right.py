"""

Given a string, compute recursively a new string where all the
lowercase 'x' chars have been moved to the end of the string.


endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
"""


def move_to_right(s, char):
    if len(s) == 1:
        return s

    if len(s) == 2:
        if s[0] == char:
            return s[1] + s[0]
        return s

    left = move_to_right(s[:1], char)
    right = move_to_right(s[1:], char)

    if left == char:
        return right + left

    return left + right


s = move_to_right('bcxxx', 'x')
print(s)
