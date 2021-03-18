# pylint:skip-file


def decimal_to_hex(n):
    # store hex in the result string
    result = ''
    # define hex char limit
    hex_char = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
    # until number is greater than 0, run loop
    while n > 0:
        # store remainder in the reverse order. if number id beyond 9, use
        # hex_char dict to convert the remainder.
        result = str(hex_char[n % 16]) + result
        # divide number by 16
        n //= 16
    return '0x' + result


print(decimal_to_hex(45))
