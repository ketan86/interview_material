# pylint:skip-file


def binary_to_decimal(n):
    result = 0
    i = len(n) - 1
    while i >= 0:
        result += int(n[i]) * (2 ** (len(n) - 1 - i))
        i -= 1
    return result


print(binary_to_decimal('1101'))
