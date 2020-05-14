# pylint:skip-file


def decimal_to_binary(n):
    result = ''
    while n > 0:
        result = str((n % 2)) + result
        n //= 2
    return result


print(decimal_to_binary(4000))
