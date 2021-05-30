# pylint:skip-file


def decimal_to_binary(n):
    # store binary in the result string
    result = ''
    # until decimal is greater than 0, run the loop
    while n > 0:
        # store remainder in the reverse order.
        #   12  -> 12 % 2 -> 0
        #          12 // 2 -> 6
        #    6  -> 6 % 2 -> 0
        #           6 // 2 -> 3
        #    3  -> 3 % 2 -> 1
        #           3 // 2 -> 1
        #    1 -> 1 % 2 -> 1
        #           1 // 2 -> 0
        #    0 -> break
        result = str((n % 2)) + result
        # divide the by 2
        n //= 2
    return result


print(decimal_to_binary(4000))
