# pylint:skip-file


def decimal_to_hex(n):
    result = ''
    letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    while n > 0:
        result = str(letters[n % 16]) + result
        n //= 16
    return '0x' + result


print(decimal_to_hex(45))
