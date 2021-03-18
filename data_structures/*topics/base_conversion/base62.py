# pylint:skip-file
from string import ascii_letters, digits


def base62(n):
    """
    With this encoding if we have to encode a number up-to 6 chars,
    we can have 62 ** 6 total combinations => 0 - 56800235583

    at each place we can put any of the 62 characters. so for 6 places
    we can have 62 * 62 * 62 * 62 * 62 * 62 total combinations.
    """
    # store result
    result = ''
    chars = digits + ascii_letters

    if n == 0:
        return chars[0]

    while n > 0:
        result = result + chars[n % 62]
        n //= 62

    return result


print(base62(0))
print(base62(1))
print(base62(12))
print(base62(62))
print(base62(123))
print(base62(1234))
print(base62(12345))
print(base62(123456))
print(base62(56800235583))
