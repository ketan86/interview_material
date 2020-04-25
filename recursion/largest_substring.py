"""

Given a string and a non-empty substring sub, compute recursively the
largest substring which starts and ends with sub and return its length.


strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
"""


def largest_substring(s, sub):
    sub_len = len(sub)

    if len(s) < sub_len:
        return 0

    if s[:sub_len] == sub and s[-sub_len:] == sub:
        return len(s)

    if s[:sub_len] == sub:
        return largest_substring(s[:-sub_len], sub)
    if s[-sub_len:0] == sub:
        return largest_substring(s[sub_len:], sub)

    return largest_substring(s[sub_len:-sub_len], sub)


n = largest_substring('catdogcat', 'cat')
print(n)
