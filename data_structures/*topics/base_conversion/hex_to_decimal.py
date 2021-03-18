# pylint:skip-file


def hex_to_decimal(n):
    # store decimal in result
    result = 0
    # define hex char dict
    hex_chars = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    # use index to find the value at each digit
    i = len(n) - 1
    # until the index is greater than 0, run the loop
    while i >= 0:
        # if it's digit, use it as it is. if not, convert using the dict.
        # forex, 1E3
        #      1 * 16 ^ 2 + 14 * 16 ^ 1 + 3 * 16 ^ 0 ->
        result += (
            int(n[i]) if n[i] not in hex_chars else hex_chars[n[i]]) * (
                16 ** (len(n) - 1 - i))
        i -= 1
    return result


print(hex_to_decimal('1c2f456d'))
