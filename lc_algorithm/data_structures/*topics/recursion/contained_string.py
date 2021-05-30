"""

Given a string that contains a single pair of parenthesis,
compute recursively a new string made of only of the
parenthesis and their contents, so "xyz(abc)123" yields "(abc)".


parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
"""


def contained_string(s):
    if len(s) < 2:
        return ''
    if s[0] == '(' and s[-1] == ')':
        return s

    if s[0] == '(':
        return contained_string(s[:-1])
    elif s[-1] == ')':
        return contained_string(s[1:])
    else:
        return contained_string(s[1:-1])


s = contained_string('abc(abca)bc')
print(s)
