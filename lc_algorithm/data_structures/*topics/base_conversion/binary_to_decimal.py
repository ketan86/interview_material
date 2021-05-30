# pylint:skip-file


def binary_to_decimal(n):
    # store decimal in result
    result = 0
    # use index far right to start calculating the decimal
    # 110010
    #      0 * 2 ^ 0 + 1 * 2 ^ 1 + ...
    i = len(n) - 1
    # until index is 0 or greater, run loop
    while i >= 0:
        result += int(n[i]) * (2 ** (len(n) - 1 - i))
        i -= 1
    return result


print(binary_to_decimal('1101'))
