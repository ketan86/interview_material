"""

Given a string, return true if it is a nesting of zero or more
pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first
and last chars, and then recur on what's inside them.


nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
"""


def nested_paranthesis(s):
    if not s:
        return True
    if len(s) == 1:
        return False

    if s[0] == '(' and s[-1] == ')':
        return nested_paranthesis(s[1:-1])
    return False


f = nested_paranthesis('((x))')
print(f)
