"""
Upper and lower case ascii letters using bitwise operator.
"""


def lower(s):
    return chr(ord(s) | ord(' '))


def upper(s):
    return chr(ord(s) & ord('_'))


print(lower('A'))
print(upper('a'))
