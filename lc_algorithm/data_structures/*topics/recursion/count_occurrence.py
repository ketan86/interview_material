"""

Count recursively the total number of "abc" and "aba" substrings
that appear in the given string.


countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
"""


def count_occurrence(s, substring):
    if len(s) < (len(substring) - 1):
        return 0

    if len(s) == len(substring):
        if s == substring:
            return 1
        return 0

    return count_occurrence(
        s[:len(substring)], substring) + count_occurrence(s[1:], substring)


n = count_occurrence('abaxxaba', 'ab')
print(n)
