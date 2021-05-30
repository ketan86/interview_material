"""

Given a string, return recursively a "cleaned" string where adjacent
chars that are the same have been reduced to a single char.
So "yyzzza" yields "yza".


stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
"""


def clean_string(s):
    if len(s) < 2:
        return s

    if len(s) == 2:
        if s[0] == s[1]:
            return s[0]
        return s

    left = clean_string(s[:2])
    right = clean_string(s[2:])

    if left[-1] == right[0]:
        return left + right[1:]
    return left + right


s = clean_string('abbccccccccbddddddsd')
print(s)
