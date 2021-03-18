"""
Given a string, compute recursively a new string where all the
adjacent chars are now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
"""


def insert_char(s, char):
    if len(s) == 1:
        return s[0]

    if len(s) == 2:
        return s[0] + char + s[1]

    return insert_char(s[:2], char) + char + insert_char(s[2:], char)


s = insert_char('abcd', '*')
print(s)
