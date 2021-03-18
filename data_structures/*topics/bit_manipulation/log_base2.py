"""Find log base 2 of 32 bit integer number"""


def find_log_base_2(num):
    """ log2(8) -> 3
        log2(64) -> 6
    """
    result = 0
    # until number is greater than 1, right shift (divide by 2)
    # and keep counting the shift
    while num > 1:
        result += 1
        num >>= 1
    return result


print(find_log_base_2(8))
