# pylint:skip-file


def hex_to_decimal(n):
    result = 0
    letters = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    i = len(n) - 1
    while i >= 0:
        result += (
            int(n[i]) if n[i] not in letters else letters[n[i]]) * (
                16 ** (len(n) - 1 - i))
        i -= 1
    return result


print(hex_to_decimal('1c2f456d'))
