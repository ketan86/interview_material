"""
Upper and lower case ascii letters using bitwise operator.
"""


def lower(s):
    """Any upper case char | ord(' ') -> 32 gives the number that
    represents the lower case char of the input.
    """
    return chr(ord(s) | ord(' '))


def upper(s):
    """Any lower case char & ord('_') -> 95 gives the number that
    represents the upper case char of the input.
    """
    return chr(ord(s) & ord('_'))


# If you look in the ASCII table you can see that the value of the character
# 'a' is 97 (decimal) and the character 'A' is 65. That is a difference of 32.
# So to convert from one to the other, add or subtract that number.

def lower_simple(s):
    return chr(ord(s) + 32)


def upper_simple(s):
    return chr(ord(s) - 32)


print(lower('A'))
print(upper('a'))
